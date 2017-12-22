"""
ID: warwick2
LANG: PYTHON3
TASK: billboard
"""
with open('billboard.in', 'r') as fin:
    in_text = fin.read().strip()
    lines = in_text.split('\n')

billboard0 = lines[0].split(' ')
billboard0 = list(map(lambda x: int(x), billboard0))
billboard1 = lines[1].split(' ')
billboard1 = list(map(lambda x: int(x), billboard1))
truck = lines[2].split(' ')
truck = list(map(lambda x: int(x), truck))

width0 = billboard0[2]-billboard0[0]
height0 = billboard0[3]-billboard0[1]
width1 = billboard1[2]-billboard1[0]
height1 = billboard1[3]-billboard1[1]

total = width0*height0 + width1*height1

print(total)

for x in range(billboard0[0], billboard0[2]):
    for y in range(billboard0[1], billboard0[3]):
        print((x, y))
        if x >= truck[0] and x < truck[2]:
            if y >= truck[1] and y < truck[3]:
                total -= 1

for x in range(billboard1[0], billboard1[2]):
    for y in range(billboard1[1], billboard1[3]):
        if x >= truck[0] and x < truck[2]:
            if y >= truck[1] and y < truck[3]:
                total -= 1

print(total)

out = str(total)
out += '\n'
with open('billboard.out', 'w') as fout:
    fout.write(out)