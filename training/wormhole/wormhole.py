"""
ID: warwick2
LANG: PYTHON3
TASK: wormhole
"""
import math

with open('wormhole.in', 'r') as fin:
    in_text = fin.read().strip()
    lines = in_text.split('\n')

num = int(lines[0])
holes = []
for i in range(1, 1+num):
    x, y = lines[i].split(' ')
    x = int(x)
    y = int(y)
    holes.append((x, y))

valid = 0


out = str(valid)
out += '\n'
with open('wormhole.out', 'w') as fout:
    fout.write(out)