input_file = open('input.txt', 'r')
line = input_file.readline()
input_file.close()

values = map(int, line.split())

output_file = open('output.txt', 'w')
output_file.write(str(values[0] + values[1]))
output_file.close()