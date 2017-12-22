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

running = {}
entries = [] # (day, cow, change)
for line in lines[1:]:
    day, cow, change = line.split(' ')
    day = int(day)
    change = int(change)
    running[cow] = g
    entries.append((day, cow, change))

entries = sorted(entries, key=lambda x: x[0])
first_day = entries[0][0]
last_day = entries[-1][0]

# print(entries)

def pick_top():
    # look for all cows with top value
    all_cows = []
    for cow in running:
        all_cows.append((cow, running[cow]))
    all_cows = sorted(all_cows, key=lambda x: x[1], reverse=True)

    top = []
    for cow in all_cows:
        if cow[1] == all_cows[0][1]: # if cow has top score
            top.append(cow[0])
        else:
            break
    top = sorted(top)
    return top

num_changes = 0
next_entry = 0

prev = pick_top()
total_entries = len(entries)
for day in range(first_day, last_day+1):
    while entries[next_entry][0] == day:
        entry = entries[next_entry]
        running[entry[1]] += entry[2]
        next_entry += 1
        if next_entry == total_entries:
            break
    top = pick_top()
    if top != prev:
        num_changes += 1
        prev = top

out = str(num_changes)
out += '\n'
with open('measurement.out', 'w') as fout:
    fout.write(out)
