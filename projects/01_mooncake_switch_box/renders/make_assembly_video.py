"""Render assembly_animation.scad frame by frame and encode an MP4 with ffmpeg.

Usage (from anywhere):  python make_assembly_video.py [--seconds 10] [--fps 30] [--jobs 10]
Frames are OpenSCAD previews of the already-exported STLs (colour needs preview mode);
re-export the STLs first if the model changed.
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent
WORKSPACE = PROJECT.parent.parent
SCENE = HERE / "assembly_animation.scad"
OPENSCAD = os.environ.get("OPENSCAD_EXE", r"C:\Program Files\OpenSCAD\openscad.com")
CAMERA = "0,0,30,58,0,0,290"


def render_frame(args):
    i, t, out_dir, size = args
    out = out_dir / f"frame_{i:04d}.png"
    env = dict(os.environ, OPENSCADPATH=str(WORKSPACE / "docs"))
    cmd = [OPENSCAD, str(SCENE), "-D", f"$t={t:.5f}", "-o", str(out),
           f"--imgsize={size[0]},{size[1]}", f"--camera={CAMERA}", "--colorscheme=Tomorrow"]
    res = subprocess.run(cmd, env=env, capture_output=True, text=True)
    if res.returncode != 0 or not out.exists():
        raise RuntimeError(f"frame {i} failed:\n{res.stderr[-2000:]}")
    return i


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seconds", type=float, default=12)
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--jobs", type=int, default=10)
    ap.add_argument("--size", type=int, nargs=2, default=[1280, 720])
    ap.add_argument("-o", "--output", default=str(PROJECT / "mooncake_switch_box_assembly.mp4"))
    a = ap.parse_args()

    n = int(a.seconds * a.fps)
    frames = Path(tempfile.mkdtemp(prefix="mooncake_frames_", dir=HERE))
    try:
        jobs = [(i, i / (n - 1), frames, a.size) for i in range(n)]
        with ThreadPoolExecutor(a.jobs) as pool:
            for done, _ in enumerate(pool.map(render_frame, jobs), 1):
                if done % 30 == 0 or done == n:
                    print(f"{done}/{n} frames", flush=True)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(a.fps),
                        "-i", str(frames / "frame_%04d.png"), "-c:v", "libx264",
                        "-pix_fmt", "yuv420p", "-crf", "18", a.output], check=True)
        shutil.copy(frames / f"frame_{n // 2:04d}.png", HERE / "assembly_video_midframe.png")
    finally:
        shutil.rmtree(frames, ignore_errors=True)
    print("wrote", a.output)


if __name__ == "__main__":
    sys.exit(main())
