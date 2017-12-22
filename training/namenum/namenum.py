"""
ID: warwick2
LANG: PYTHON3
TASK: namenum
"""
with open('namenum.in', 'r') as fin:
    in_text = fin.read().strip()
    lines = in_text.split('\n')

with open('dict.txt', 'r') as name_file:
    names = name_file.read().strip().split('\n')

letters = {
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y'],
}
reverse_letters = {}
for num in letters:
    for letter in letters[num]:
        reverse_letters[letter] = num
    
nums = lines[0]
length = len(nums)

possible_names = []
for name in names:
    # Check length
    if len(name) == length:
        # Check all letters:
        good = True
        for i, letter in enumerate(name):
            if letter in ['Q', 'Z']:
                good = False
                break
            if reverse_letters[letter] == int(nums[i]):
                continue
            good = False
            break

        # Add if all letters pass
        if good:
            possible_names.append(name)

if not possible_names:
    out = 'NONE\n'
else:
    out = '\n'.join(possible_names)
    out += '\n'

with open('namenum.out', 'w') as fout:
    fout.write(out)