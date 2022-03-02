#!/usr/bin/env python3

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from commonplot import plt

def f(x):
    return 5*x**2 + 3*x + 25

x = list(range(-10, 10+1))
y = [f(i) for i in x]

fig = plt.figure(figsize=(4, 3))

plt.xlabel(r'asdf - this is my practise 500 (hg)')
plt.ylabel(r'$\alpha$')

plt.plot(x, y, label=r'$\beta+\alpha+\gamma$')
plt.legend()

plt.tight_layout()
plt.savefig("plot.pgf")
plt.savefig("plot.pdf")

# plt.show()
