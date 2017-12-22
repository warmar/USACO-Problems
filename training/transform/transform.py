"""
ID: warwick2
LANG: PYTHON3
TASK: transform
"""
import sys

with open('transform.in', 'r') as fin:
    in_text = fin.read().strip()
    lines = in_text.split('\n')

n = int(lines[0])
square0 = []
square1 = []
newline = ['' for _ in range(n)]

for i in range(n):
    square0.append(newline[:])
    square1.append(newline[:])
    for j in range(n):
        square0[i][j] = lines[i+1][j]
        square1[i][j] = lines[n+i+1][j]

def rot90(square):
    out = []
    for _ in range(n):
        out.append(newline[:])

    for i in range(n):
        for j in range(n):
            topd=i
            leftd=j

            new_topd=leftd
            new_rightd=topd
            new_leftd=(n-1)-new_rightd
            
            out[new_topd][new_leftd] = square[i][j]
    
    return out

def reflect(square):
    out = []
    for i in range(n):
        out.append(newline[:])
        for j in range(n):
            topd=i
            leftd=j

            new_topd=topd
            new_rightd=leftd
            new_leftd=(n-1)-new_rightd
            
            out[new_topd][new_leftd] = square[i][j]
    
    return out

# Check all
def done():
    out = str(num)
    out += '\n'
    with open('transform.out', 'w') as fout:
        fout.write(out)
    sys.exit(0)

num = None

sq90 = rot90(square0)
if sq90 == square1:
    num = 1
    done()

sq180 = rot90(sq90)
if sq180 == square1:
    num = 2
    done()

sq270 = rot90(sq180)
if sq270 == square1:
    num = 3
    done()

sqref = reflect(square0)
if sqref == square1:
    num = 4
    done()

sq90ref = reflect(sq90)
if sq90ref == square1:
    num = 5
    done()
sq180ref = reflect(sq180)
if sq180ref == square1:
    num = 5
    done()
sq270ref = reflect(sq270)
if sq270ref == square1:
    num = 5
    done()

if square0 == square1:
    num = 6
    done()

num = 7
done()