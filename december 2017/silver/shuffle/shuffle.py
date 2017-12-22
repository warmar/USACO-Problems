"""
ID: warwick2
LANG: PYTHON3
TASK: shuffle
"""
with open('shuffle.in', 'r') as fin:
    in_text = fin.read().strip()
    lines = in_text.split('\n')

n = int(lines[0])
shuffle = [int(x)-1 for x in lines[1].split()]

for _ in range(n):
    



out = ''
out += '\n'

with open('shuffle.out', 'w') as fout:
    fout.write(out)
