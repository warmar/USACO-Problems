"""
ID: warwick2
LANG: PYTHON2
TASK: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')

name,group=fin.read().split('\n')[:-1]

letters='abcdefghijklmnopqrstuvwxyz'
dic = {}

for i, letter in zip(range(len(letters)), letters):
	dic[letter] = i+1

name_product = 1
for letter in name:
	name_product *= dic[letter.lower()]
name_mod = name_product % 47

group_product = 1
for letter in group:
	group_product *= dic[letter.lower()]
group_mod = group_product % 47

if name_mod == group_mod:
	fout.write('GO\n')
else:
	fout.write('STAY\n')

fout.close()