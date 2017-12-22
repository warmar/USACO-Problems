"""
ID: warwick2
LANG: PYTHON3
TASK: art
"""

with open('art.in', 'r') as fin:
    in_text = fin.read().strip()
    lines = in_text.split('\n')

n = int(lines[0])

square = [[0 for _ in range(n)] for _ in range(n)]
color_positions = {}
color_corners = {}

for i in range(n):
    for j in range(n):
        pos = (i, j)

        color = int(lines[1+i].split(' ')[j])
        square[i][j] = color

        if color == 0:
            continue
        
        if color not in color_positions:
            color_positions[color] = set()
            color_corners[color] = [i, j, i, j]
        else:
            corners = color_corners[color]
            color_corners[color] = [min(i, corners[0]), min(j, corners[1]), max(i, corners[2]), max(j, corners[3])]

        color_positions[color].add(pos)

possible_first = n**2

for color in color_positions:
    positions = color_positions[color]
    for position in positions:
        i, j = position

        num_recs = 0
        for color_ in color_corners:
            if color == color_:
                continue

            corners = color_corners[color_]
            if i in range(corners[0], corners[2]+1) and j in range(corners[1], corners[3]+1):
                num_recs += 1
                possible_first -= 1
                break
        if num_recs >= 1:
            break

out = str(possible_first)
out += '\n'
with open('art.out', 'w') as fout:
    fout.write(out)