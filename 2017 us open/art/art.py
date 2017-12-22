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

visible_colors = set()
zeros = set()
all_pos = set()
color_positions = {}
color_corners = {}

for i in range(n):
    for j in range(n):
        pos = (i, j)
        all_pos.add(pos)

        color = int(lines[1+i].split(' ')[j])
        visible_colors.add(color)

        if color == 0:
            zeros.add(pos)
        
        square[i][j] = color

colors = range(1, n**2+1)

possible_first = 0
all_colors = []
all_corners = []
all_positions = []

unchecked = all_pos.copy().difference(zeros)
for color in colors:
    if color not in visible_colors: # color not visible
        possible_first += 1
        continue

    corners = [n, n, 0, 0] # topleft, bottomright
    topmost = n
    leftmost = n
    bottommost = 0
    rightmost = 0

    found = set()
    for pos in unchecked:
        i, j = pos
        iscolor = square[i][j] == color
        if iscolor:
            corners[0] = min(i, corners[0]) # top
            corners[1] = min(j, corners[1]) # left
            corners[2] = max(i, corners[2]) # bottom
            corners[3] = max(j, corners[3]) # right
            found.add(pos)
    unchecked.difference_update(found)

    all_colors.append(color)
    all_corners.append(corners)
    all_positions.append(found)

for i, color in enumerate(all_colors):
    overlaps = False

    over_corners = all_corners[i]
    positions = all_positions[i]
    for pos in positions:
        y, x = pos
        for i_, under_corners in enumerate(all_corners):
            if i == i_:
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