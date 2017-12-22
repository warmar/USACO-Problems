"""
ID: warwick2
LANG: PYTHON3
TASK: dualpal
"""
with open('dualpal.in', 'r') as fin:
    in_text = fin.read().strip()
    lines = in_text.split('\n')

n, s = lines[0].split(' ')
n = int(n)
s = int(s)

def tobase(num, base):
    curr = num
    digits = []
    while curr >= base:
        curr, digit = divmod(curr, base)
        digits.insert(0, digit)
    digits.insert(0, curr)

    out = ''
    for digit in digits:
        out += str(digit)

    return out

def ispal(string):
    check, _ = divmod(len(string), 2)
    good = True
    for pos in range(check):
        if string[pos] != string[-(pos+1)]:
            good = False
            break
    return good

dualpals = []
i = s
while len(dualpals) < n:
    i += 1
    num_pals = 0
    for base in range(2, 11):
        if ispal(tobase(i, base)):
            num_pals += 1
            if num_pals == 2:
                dualpals.append(i)
                break

print(dualpals)

out = ''
for dualpal in dualpals:
    out += str(dualpal) + '\n'

with open('dualpal.out', 'w') as fout:
    fout.write(out)