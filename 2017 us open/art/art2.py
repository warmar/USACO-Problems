"""
ID: warwick2
LANG: PYTHON3
TASK: art
"""

with open('art.in', 'r') as fin:
    in_text = fin.read().strip()
    lines = in_text.split('\n')

n = int(lines[0])

color_positions = {}
color_corners = {}

for i in range(n):
    for j in range(n):
        pos = (i, j)

        color = int(lines[1+i].split(' ')[j])

        if color == 0:
            continue
        
        if color not in color_positions:
            color_positions[color] = set()
            color_corners[color] = [i, j, i, j]
        else:
            corners = color_corners[color]
            color_corners[color] = [min(i, corners[0]), min(j, corners[1]), max(i, corners[2]), max(j, corners[3])]

        color_positions[color].add(pos)

colors = range(1, n**2+1)

possible_first = 0

for color in colors:
    if color not in color_positions: # color not visible
        possible_first += 1
        continue

    overlaps = False
    over_corners = color_corners[color]
    positions = color_positions[color]

    for pos in positions:
        y, x = pos
        for under_corners in color_corners.values():
            if under_corners == over_corners:
                continue

            if y in range(max(under_corners[0], over_corners[0]), min(under_corners[2]+1, over_corners[2]+1)):
                if x in range(max(under_corners[1], over_corners[1]), min(under_corners[3]+1, over_corners[3]+1)):
                    overlaps = True
                    break
        
        if overlaps:
            break
    
    if not overlaps:
        possible_first += 1

out = str(possible_first)
out += '\n'
with open('art.out', 'w') as fout:
    fout.write(out)