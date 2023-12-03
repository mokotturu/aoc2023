from collections import defaultdict
import math

def main(file):
	schematic = []

	lines = file.read().splitlines()
	for line in lines:
		schematic.append(line)

	gears = defaultdict(list)

	for line_idx, line in enumerate(schematic):
		is_part_number = False
		temp_num = ''
		gear = None

		for char_idx, char in enumerate(line):
			if char.isdigit():
				temp_num += char

				if char_idx == len(line) - 1:
					if is_part_number:
						gears[gear].append(int(temp_num))
					is_part_number = False
					temp_num = ''

				if is_part_number:
					continue

				if char_idx > 0:
					if schematic[line_idx][char_idx - 1] == '*':
						is_part_number = True
						gear = (line_idx, char_idx - 1)
						continue
				if char_idx < len(line) - 1:
					if schematic[line_idx][char_idx + 1] == '*':
						is_part_number = True
						gear = (line_idx, char_idx + 1)
						continue
				if line_idx > 0:
					if schematic[line_idx - 1][char_idx] == '*':
						is_part_number = True
						gear = (line_idx - 1, char_idx)
						continue
				if line_idx < len(schematic) - 1:
					if schematic[line_idx + 1][char_idx] == '*':
						is_part_number = True
						gear = (line_idx + 1, char_idx)
						continue
				if char_idx > 0 and line_idx > 0:
					if schematic[line_idx - 1][char_idx - 1] == '*':
						is_part_number = True
						gear = (line_idx - 1, char_idx - 1)
						continue
				if char_idx < len(line) - 1 and line_idx > 0:
					if schematic[line_idx - 1][char_idx + 1] == '*':
						is_part_number = True
						gear = (line_idx - 1, char_idx + 1)
						continue
				if char_idx > 0 and line_idx < len(schematic) - 1:
					if schematic[line_idx + 1][char_idx - 1] == '*':
						is_part_number = True
						gear = (line_idx + 1, char_idx - 1)
						continue
				if char_idx < len(line) - 1 and line_idx < len(schematic) - 1:
					if schematic[line_idx + 1][char_idx + 1] == '*':
						is_part_number = True
						gear = (line_idx + 1, char_idx + 1)
						continue
			else:
				if is_part_number:
					gears[gear].append(int(temp_num))
				is_part_number = False
				temp_num = ''

	print(sum([math.prod(gears[key]) for key in gears.keys() if len(gears[key]) == 2]))
