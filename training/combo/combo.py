"""
ID: warwick2
LANG: PYTHON3
TASK: combo
"""
with open('combo.in', 'r') as fin:
    in_text = fin.read().strip()
    lines = in_text.split('\n')

n = int(lines[0])
combo1 = lines[1].split(' ')
combo2 = lines[2].split(' ')
tolerance = 2

settings = set()

def k(combo):
    bad_i0 = set()
    bad_i1 = set()
    bad_i2 = set()
    for i0 in range(1, n+1):
        if i0 in bad_i0:
            continue
        for i1 in range(1, n+1):
            if i1 in bad_i1:
                continue
            for i2 in range(1, n+1):
                if i2 in bad_i2:
                    continue

                num0 = int(combo[0])
                num1 = int(combo[1])
                num2 = int(combo[2])
                
                if abs(num0-i0) > tolerance:
                    if not (num0 == 1 and i0 in [n-1, n]):
                        if not (num0 == 2 and i0 in [n]):
                            if not (num0 == n-1 and i0 in [1]):
                                if not (num0 == n and i0 in [1, 2]):
                                    bad_i0.add(i0)
                                    continue
                if abs(num1-i1) > tolerance:
                    if not (num1 == 1 and i1 in [n-1, n]):
                        if not (num1 == 2 and i1 in [n]):
                            if not (num1 == n-1 and i1 in [1]):
                                if not (num1 == n and i1 in [1, 2]):
                                    bad_i1.add(i1)
                                    continue
                if abs(num2-i2) > tolerance:
                    if not (num2 == 1 and i2 in [n-1, n]):
                        if not (num2 == 2 and i2 in [n]):
                            if not (num2 == n-1 and i2 in [1]):
                                if not (num2 == n and i2 in [1, 2]):
                                    bad_i2.add(i2)
                                    continue

                settings.add((i0, i1, i2))

k(combo1)
k(combo2)

out = str(len(settings))
out += '\n'
with open('combo.out', 'w') as fout:
    fout.write(out)
