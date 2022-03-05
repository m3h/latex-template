#!/usr/bin/env python3

import paperconf

import matplotlib.pyplot as plt
import matplotlib


def apply_tex_config():
    matplotlib.use('pgf')
    
    plt.rcParams.update({
        "font.family": 'serif',
        "font.serif": [paperconf.mehfont],
        "font.sans-serif": [paperconf.mehfont],
        "font.monospace": [paperconf.mehfont],
        # Only available in Python 3.9+
        # "font.size": paperconf.mehfontsize.removesuffix('pt'),
        "font.size": paperconf.mehfontsize.split('pt')[0],
        "text.usetex": True,
        "pgf.preamble": paperconf.mehtex_preamble,
        "pgf.texsystem": 'lualatex',
        "axes.unicode_minus": True,
    })

apply_tex_config()

if __name__ == "__main__":
    plt.plot([1,3,5], [2,4 ,6])
    plt.savefig("tplot.pgf")
    plt.savefig("tplot.pdf")
