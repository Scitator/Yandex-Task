from datetime import datetime

def f(x):
    return {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday',
    }[x]

input_file = open('input.txt', 'r')
line = input_file.readline()

while line:
	date_object = datetime.strptime(line.strip(), '%d %B %Y')
	print f(date_object.weekday())
	line = input_file.readline()
    
input_file.close()