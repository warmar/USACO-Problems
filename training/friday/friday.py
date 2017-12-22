"""
ID: warwick2
LANG: PYTHON3
TASK: friday
"""
with open('friday.in', 'r') as fin:
    in_text = fin.read()

start_year = 1900
years = int(in_text)

hits = [0, 0, 0, 0, 0, 0, 0]
months = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 2
for i in range(start_year, start_year+years):
    leap = i % 4==0 and (i%100 != 0 or i % 400 == 0)
    months[1] = 29 if leap else 28
    days = 366 if leap else 365

    date = 1
    month = 0
    for _ in range(days):
        if date == 13:
            hits[day] += 1

        if (date+1) % months[month] == 1:
            date = 1
            month += 1
        else:
            date += 1
        
        day += 1
        day = day % 7
    
out = ' '.join([str(x) for x in hits])
out += '\n'
with open('friday.out', 'w') as fout:
    fout.write(out)
