"""
ID: warwick2
LANG: PYTHON3
TASK: learning
"""
import bisect

with open('learning.in', 'r') as fin:
    in_text = fin.read().strip()
    lines = in_text.split('\n')

n, a, b = lines[0].split(' ')
n = int(n)
a = int(a)
b = int(b)
weights = []
data = {}
for line in lines[1:n+1]:
    spots, weight = line.split(' ')
    spots = spots=='S'
    weight = int(weight)
    data[weight] = spots
    weights.append(weight)

weights = sorted(weights)
num_have_spots = 0

left_turn_points = []
spots_ranges = []
outliers = []

for i, weight in enumerate(weights):
    spots_ranges.append(data[weight])

    if i == len(weights)-1: # last max point is last weight
        left_turn_points.append(weight)
        continue

    next_weight = weights[i+1]
    d_to_next = next_weight-weight

    gap, no_outlier = divmod(d_to_next, 2)
    
    if not no_outlier:
        outliers.append(weight+gap)
        left_turn_points.append(weight+gap)
    else:
        left_turn_points.append(weight+gap+1)


print(weights)
print(left_turn_points)
print(spots_ranges)
print(outliers)

first = True
for i, turn_point in enumerate(left_turn_points):
    if a > turn_point:
        continue

    spots = spots_ranges[i]
    outlier = turn_point in outliers

    if first:
        first = False
        if spots:
            num_have_spots += turn_point-a
    else:
        if spots:
            num_have_spots += turn_point-left_turn_points[i-1]
        if outlier:
            if spots or left_turn_points[i+1]:
                num_have_spots += 1

        # last equals b
        if turn_point == b:
            break
        # last after b
        if turn_point > b:
            if outlier:
                num_have_spots += b-turn_point
            break
        # last before b
        if i == len(left_turn_points)-1:
            num_have_spots += b-turn_point

out = str(num_have_spots)
out += '\n'
with open('learning.out', 'w') as fout:
    fout.write(out)