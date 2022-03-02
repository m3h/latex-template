#!/usr/bin/env python3


def _load_conf(confpaper_rel_path=None, mehtex_common_rel_path=None):

    if confpaper_rel_path is None:
        confpaper_rel_path = 'src/lua/confpaper.lua'
    if mehtex_common_rel_path is None:
        mehtex_common_rel_path = 'src/tex/mehtex-common.tex'

    from pathlib import Path

    import lupa
    from lupa import LuaRuntime
    lua = LuaRuntime(unpack_returned_tuples=True)

    conf_path = confpaper_rel_path
    mehtex_common_path = mehtex_common_rel_path

    # load mehtex preamble
    with open(mehtex_common_path) as f:
        mehtex_preamble = f.read()

    # load conf file
    confpaper = None
    with open(conf_path) as f:
        conf_str = f.read()
        lua.execute(conf_str)

        lua_globals = lua.globals()
        confpaper = lua_globals.conf
        confpaper = dict(confpaper)
   
        lua_preamble = list()
        lua_preamble += ['%%% start confpaper.lua - LUA generated %%%'] 
        for k, v in confpaper.items():
            newcmd = f'\\newcommand{{\\{k}}}{{{v}}}'
            lua_preamble += [newcmd]
        lua_preamble += ['%%% end confpaper.lua - LUA generated %%%'] 
        lua_preamble += [mehtex_preamble]

        mehtex_preamble = '\n'.join(lua_preamble)

        confpaper['mehtex_preamble'] = mehtex_preamble

        globals().update(confpaper)

_load_conf()
