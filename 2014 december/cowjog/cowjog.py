"""
ID: warwick2
LANG: PYTHON3
TASK: cowjog
"""
with open('cowjog.in', 'r') as fin:
    in_text = fin.read().strip()
    lines = in_text.split('\n')

n = int(lines[0])
cows = [] # (pos, speed)
for line in lines[1:n+1]:
    pos, speed = line.split(' ')
    pos = int(pos)
    speed = int(speed)
    cows.append([pos, speed])

groups = 0
cows = sorted(cows, key=lambda cow: cow[0])
i = len(cows)-1
while i >= 0:
    cow = cows[i]
    if i == len(cows)-1: # handle last cow
        groups += 1
        i -= 1
        continue
    
    if cows[i+1][1] >= cow[1]: # if next cow is faster or same speed
        groups += 1
    else: # if next cow is slower, no new group, change effective speed
        cows[i][1] = cows[i+1][1]
    i -= 1

out = str(groups)
out += '\n'
with open('cowjog.out', 'w') as fout:
    fout.write(out)