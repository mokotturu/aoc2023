def main(file):
	line = file.read()
	strings = line.split(',')

	current_values = []
	for string in strings:
		current_value = 0
		for char in string:
			current_value += ord(char)
			current_value *= 17
			current_value %= 256
		current_values.append(current_value)

	print(sum(current_values))
