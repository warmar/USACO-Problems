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
final_positions = [int(x) for x in lines[2].split()]

reverse = {}

for i in range(n):
    reverse[shuffle[i]] = i

print(reverse)

def do_reverse(order):
    out = [0]*n
    for i in range(n):
        cow = order[i]
        out[reverse[i]] = cow
    return out

pos2 = do_reverse(final_positions)
pos1 = do_reverse(pos2)
pos0 = do_reverse(pos1)

print(pos0)

out = ''
for cow in pos0:
    out += '%s\n' % cow

with open('shuffle.out', 'w') as fout:
    fout.write(out)