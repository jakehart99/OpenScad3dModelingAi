# Rebuilds every printable STL (+ validation JSON) for the mooncake switch box.
# Run from anywhere:  powershell -ExecutionPolicy Bypass -File build.ps1
$ErrorActionPreference = 'Stop'
$proj  = $PSScriptRoot
$tools = Join-Path $proj '..\..\tools\openscad_tools.py'
$scad  = Join-Path $proj 'mooncake_switch_box.scad'

function Build-Part($part, $out, $extra = @()) {
    $defs = @('-D', "part=`"$part`"") + $extra
    python $tools export $scad @defs -o $out
    if ($LASTEXITCODE -ne 0) { throw "export failed: $out" }
    python $tools check $out --json ($out -replace '\.stl$', '.validation.json')
}

foreach ($p in 'base', 'insert', 'insert_single', 'lid', 'fit_coupon') {
    Build-Part $p (Join-Path $proj "$p.stl")
}
foreach ($c in 'red', 'yellow', 'white') {
    Build-Part 'lid_inlay' (Join-Path $proj "lid_inlay_$c.stl") @('-D', "inlay_color=`"$c`"")
}
New-Item -ItemType Directory -Force (Join-Path $proj 'keycaps') | Out-Null
foreach ($d in 'smiley', 'zhong', 'qiu', 'yue', 'man', 'jia', 'le', 'yuan', 'fu', 'blank') {
    Build-Part 'keycap' (Join-Path $proj "keycaps\keycap_$d.stl") @('-D', "design=`"$d`"")
}
