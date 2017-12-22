"""
ID: warwick2
LANG: PYTHON3
TASK: measurement
"""
with open('measurement.in', 'r') as fin:
    in_text = fin.read().strip()
    lines = in_text.split('\n')

n, g = lines[0].split(' ')
n = int(n)
g = int(g)

entries = [] # (day, cow, change)
for line in lines[1:]:
    day, cow, change = line.split(' ')
    day = int(day)
    change = int(change)
    entries.append((day, cow, change))

entries = sorted(entries, key=lambda x: x[0])
first_day = entries[0][0]
last_day = entries[-1][0]

print(entries)

# Start all cows at 7
running_count = {}
for entry in entries:
    cow = entry[1]
    if cow in running_count:
        continue
    running_count[cow] = g

current_top = None
num_changes = 0

def pick_top():
    # super simple, look for all cows with top value
    all_cows = []
    for cow in running_count:
        all_cows.append((cow, running_count[cow]))
    all_cows = sorted(all_cows, key=lambda x: x[1], reverse=True)

    top = []
    for cow in all_cows:
        if cow[1] == all_cows[0][1]: # if cow has top score
            top.append(cow[0])
        else:
            break
    top = sorted(top)
    return top

current_top = pick_top()

print(current_top)

for day in range(first_day, last_day+1):
    for entry in entries:
        if entry[0] == day:
            # update cow on day
            cow = entry[1]
            change = entry[2]
            running_count[cow] += change
    new_top = pick_top()
    if current_top != new_top:
        num_changes += 1
        current_top = new_top

out = str(num_changes)
out += '\n'
with open('measurement.out', 'w') as fout:
    fout.write(out)