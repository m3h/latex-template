# Use LuaLaTeX
$pdf_mode = 4;

# Set the output directory (we don't want to clutter our main locs)
$out_dir = "build" ;
# Sets the output directory of auxillary files
# $aux_dir = "build/aux/" ;
# Most engines don't actually support it, but latexmkrc can emulate the effect
$emulate_aux = 1;
