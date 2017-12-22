"""
ID: warwick2
LANG: PYTHON3
TASK: crypt1
"""
with open('crypt1.in', 'r') as fin:
    in_text = fin.read().strip()
    lines = in_text.split('\n')

n = int(lines[0])
nums = lines[1].split(' ')

# possible = 0
# for i in range(n):
#     num1 = int(nums[i]*3)
#     num2 = int(nums[i]*2)

#     tot = num1*num2
#     if len(str(tot)) != 4:
#         continue

#     first_p = int(nums[i])*num1
#     if len(str(first_p)) != 3:
#         continue

#     possible += 1


possible = 0
for i in range(n**3): # find first number
    _, i1 = divmod(i, n)
    _, i2 = divmod(_, n)
    _, i3 = divmod(_, n)

    num1 = int(nums[i1]+nums[i2]+nums[i3])

    for j in range(n**2): # find second number
        _, j1 = divmod(j, n)
        _, j2 = divmod(_, n)

        num2 = int(nums[j1]+nums[j2])

        tot = num1*num2
        if len(str(tot)) != 4:
            continue

        good = True
        for digit in str(tot):
            if digit not in nums:
                good = False
                break
        if not good:
            continue

        first_p = int(nums[j2])*num1
        if len(str(first_p)) != 3:
            continue

        good = True
        for digit in str(first_p):
            if digit not in nums:
                good = False
                break
        if not good:
            continue

        second_p = int(nums[j1])*num1
        if len(str(second_p)) != 3:
            continue

        good = True
        for digit in str(second_p):
            if digit not in nums:
                good = False
                break
        if not good:
            continue

        possible += 1

print(possible)
out = str(possible)
out += '\n'
with open('crypt1.out', 'w') as fout:
    fout.write(out)
