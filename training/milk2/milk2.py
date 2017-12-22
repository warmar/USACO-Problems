"""
ID: warwick2
LANG: PYTHON3
TASK: milk2
"""
import bisect

with open('milk2.in', 'r') as fin:
    in_text = fin.read().strip()

lines = in_text.split('\n')

n = int(lines[0])

farmers = []
for line in lines[1:]:
    start, stop = line.split(' ')
    farmers.append((int(start), int(stop)))

times = []
toggles = []
for farmer in farmers:
    start, stop = farmer

    # start
    start_insertion = bisect.bisect_left(times, start)
    if start_insertion != 0:
        # prev_time = times[start_insertion-1]
        prev_toggle = toggles[start_insertion-1]
        if prev_toggle is False:
            # insert start
            times.insert(start_insertion, start)
            toggles.insert(start_insertion, True)
        else:
            # use previous start for later deletions
            start_insertion -= 1
    else:
        times.insert(start_insertion, start)
        toggles.insert(start_insertion, True)

    # stop
    stop_insertion = bisect.bisect_right(times, stop)
    if stop_insertion < len(times):
        next_time = times[stop_insertion]
        next_toggle = toggles[stop_insertion]
        if next_toggle is True:
            # next toggle is True
            times.insert(stop_insertion, stop)
            toggles.insert(stop_insertion, False)
    else:
        # last stop
        times.insert(stop_insertion, stop)
        toggles.insert(stop_insertion, False)

    # in-between
    for i in reversed(range(start_insertion+1, stop_insertion)):
        del times[i]
        del toggles[i]

print(times)
print(toggles)

longest_milking = 0
longest_idle = 0
milking = True
for i, time in enumerate(times[1:]):
    i+=1
    duration = time-times[i-1]
    if not milking:
        longest_idle = max(longest_idle, duration)
    else:
        longest_milking = max(longest_milking, duration)

    milking = not milking

out = '%s %s' % (longest_milking, longest_idle)
out += '\n'
with open('milk2.out', 'w') as fout:
    fout.write(out)