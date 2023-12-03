def main(file):
	schematic = []

	lines = file.read().splitlines()
	for line in lines:
		schematic.append(line)

	part_nums = []

	for line_idx, line in enumerate(schematic):
		is_part_number = False
		temp_num = ''

		for char_idx, char in enumerate(line):
			if char.isdigit():
				temp_num += char

				if char_idx == len(line) - 1:
					if is_part_number:
						part_nums.append(int(temp_num))
					is_part_number = False
					temp_num = ''

				if is_part_number:
					continue

				if char_idx > 0:
					if (schematic[line_idx][char_idx - 1] != '.' and
						not schematic[line_idx][char_idx - 1].isdigit()):
						is_part_number = True
						continue
				if char_idx < len(line) - 1:
					if (schematic[line_idx][char_idx + 1] != '.' and
						not schematic[line_idx][char_idx + 1].isdigit()):
						is_part_number = True
						continue
				if line_idx > 0:
					if (schematic[line_idx - 1][char_idx] != '.' and
						not schematic[line_idx - 1][char_idx].isdigit()):
						is_part_number = True
						continue
				if line_idx < len(schematic) - 1:
					if (schematic[line_idx + 1][char_idx] != '.' and
						not schematic[line_idx + 1][char_idx].isdigit()):
						is_part_number = True
						continue
				if char_idx > 0 and line_idx > 0:
					if (schematic[line_idx - 1][char_idx - 1] != '.' and
						not schematic[line_idx - 1][char_idx - 1].isdigit()):
						is_part_number = True
						continue
				if char_idx < len(line) - 1 and line_idx > 0:
					if (schematic[line_idx - 1][char_idx + 1] != '.' and
						not schematic[line_idx - 1][char_idx + 1].isdigit()):
						is_part_number = True
						continue
				if char_idx > 0 and line_idx < len(schematic) - 1:
					if (schematic[line_idx + 1][char_idx - 1] != '.' and
						not schematic[line_idx + 1][char_idx - 1].isdigit()):
						is_part_number = True
						continue
				if char_idx < len(line) - 1 and line_idx < len(schematic) - 1:
					if (schematic[line_idx + 1][char_idx + 1] != '.' and
						not schematic[line_idx + 1][char_idx + 1].isdigit()):
						is_part_number = True
						continue
			else:
				if is_part_number:
					part_nums.append(int(temp_num))
				is_part_number = False
				temp_num = ''

	print(sum(part_nums))
