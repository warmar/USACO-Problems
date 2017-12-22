"""
ID: warwick2
LANG: PYTHON3
TASK: gift1
"""
with open('gift1.in', 'r') as fin:
    in_text = fin.read()

lines = in_text.split('\n')
np = int(lines[0])
names = lines[1:np+1]
gifts = lines[np+1:]

start_balances = {}
balances = {name:0 for name in names}

reset = True
giver = None
money = 0
recipients = 0
done = 0
for line in gifts:
	if reset and giver is None:
		giver = line
		continue
	if reset and giver is not None:
		reset = False

		ls = line.split(' ')
		money = int(ls[0])
		recipients = int(ls[1])

		start_balances[giver] = money
		if recipients != 0:
			balances[giver] += divmod(money,recipients)[1]
		else:
			balances[giver] += money
			# Reset
			reset = True
			giver = None
			money = 0
			recipients = 0
			done = 0

		continue
	if not reset and giver is not None:
		balances[line] += divmod(money,recipients)[0]
		done += 1

		if done == recipients:
			# Reset
			reset = True
			giver = None
			money = 0
			recipients = 0
			done = 0
		continue

out = ''
for name in names:
	out += '%s %s\n' % (name, balances[name]-start_balances[name])

with open('gift1.out', 'w') as fout:
    fout.write(out)