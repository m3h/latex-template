dofile('./src/lua/confpaper.lua')

-- Loop through every key, value pair in conf (defined in confpaper.conf)
-- and define it as a command in LaTeX
for k, v in pairs(conf) do
	-- print("\\newcommand{\\"..k.."}{"..v.."}")
	tex.print("\\newcommand{\\"..k.."}{"..v.."}")
end
