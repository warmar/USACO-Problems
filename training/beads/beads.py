"""
ID: warwick2
LANG: PYTHON3
TASK: beads
"""
with open('beads.in', 'r') as fin:
    in_text = fin.read()

in_text = in_text.split('\n')[1]

best_n = 0

for i in range(len(in_text)):
    start_forw = None
    start_back = None

    n = 0

    curr_ind = i
    while start_forw is None or in_text[curr_ind] == start_forw or in_text[curr_ind]=='w':
        if start_forw is None and in_text[curr_ind] != 'w':
            start_forw = in_text[curr_ind]

        n += 1
        curr_ind += 1

        curr_ind = curr_ind % len(in_text)

        if curr_ind == i:
            break

    curr_ind = i-1
    while start_back is None or in_text[curr_ind] == start_back or in_text[curr_ind]=='w':
        if start_back is None and in_text[curr_ind] != 'w':
            start_back = in_text[curr_ind]

        n += 1
        curr_ind -= 1

        curr_ind = curr_ind % len(in_text)

        if curr_ind == i:
            break

    if n > len(in_text):
        n = len(in_text)

    print('i %s' % i)
    print(n)
    if n > best_n:
        best_n = n

out = str(best_n)
out += '\n'
with open('beads.out', 'w') as fout:
    fout.write(out)