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
weights = set()
data = {}
for line in lines[1:n+1]:
    spots, weight = line.split(' ')
    spots = spots=='S'
    weight = int(weight)
    data[weight] = spots
    if len(weights) > 0:
        if weight in weights: # Handle duplicate weights
            data[weight] = data[weight] or spots
        else:
            weights.add(weight)
    else:
        weights.add(weight)

weights = sorted(list(weights))
num_have_spots = 0

ranges = [] # (spots, start, end)
for i, weight in enumerate(weights):
    spots = data[weight]

    # Handle last weight:
    if i != len(weights)-1:
        next_weight = weights[i+1]
        next_spots = data[next_weight]
        d_to_next = next_weight-weight
        gap, no_outlier = divmod(d_to_next, 2)

        if no_outlier:
            max_not_included = weight+gap+1
        else:
            max_not_included = weight+gap
    else:
        max_not_included = 1000000001
        next_spots = spots
        no_outlier = 1

    if i == 0: # Handle first weight
        prev_max = 0
    else:
        prev_max = ranges[-1][2]

    ranges.append((spots, prev_max, max_not_included))
    
    if not no_outlier:
        outlier_spots = spots or next_spots
        ranges.append((outlier_spots, weight+gap, weight+gap+1)) # Add lone outlier

for spot_range in ranges:
    spots = spot_range[0]

    start_in = spot_range[1] in range(a, b+1)
    end_in = spot_range[2] in range(a, b+1)
    
    if start_in and end_in: # fully contained in [a, b]
        if spots:
            num_have_spots += spot_range[2]-spot_range[1]
        continue
    if not start_in and end_in: # a outside of range
        if spots:
            num_have_spots += spot_range[2]-a
        continue
    if start_in and not end_in: # b outside of range
        if spots:
            num_have_spots += b-spot_range[1]+1
        break

out = str(num_have_spots)
out += '\n'
with open('learning.out', 'w') as fout:
    fout.write(out)