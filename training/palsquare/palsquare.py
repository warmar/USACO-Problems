"""
ID: warwick2
LANG: PYTHON3
TASK: palsquare
"""
with open('palsquare.in', 'r') as fin:
    in_text = fin.read().strip()
    lines = in_text.split('\n')

dic = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
    16: 'G',
    17: 'H',
    18: 'I',
    19: 'J',
    20: 'K',
}

base = int(lines[0])

def tobase(num):
    curr = num
    digits = []
    while curr >= base:
        curr, digit = divmod(curr, base)
        digits.insert(0, digit)
    digits.insert(0, curr)

    out = ''
    for digit in digits:
        if digit >= 10:
            out += dic[digit]
        else:
            out += str(digit)

    return out

pals = []
for i in range(1,301):
    square = tobase(i**2)

    check, _ = divmod(len(square),2)
    good = True
    for pos in range(check):
        if square[pos] != square[-(pos+1)]:
            good = False
            break
    if good:
        pals.append(i)

out = ''
for pal in pals:
    out += '%s %s\n' % (tobase(pal), tobase(pal**2))

if not out:
    out += 'NONE\n'
with open('palsquare.out', 'w') as fout:
    fout.write(out)