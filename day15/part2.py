import re
from collections import defaultdict

def my_hash(string):
	current_value = 0
	for char in string:
		current_value += ord(char)
		current_value *= 17
		current_value %= 256
	return current_value

def main(file):
	strings = file.read().split(',')
	boxes = defaultdict(list)
	for string in strings:
		ans = re.compile(r'(\w*)(=|-)(\d*)').match(string)
		label, sign, focal_length = ans.groups()
		box_num = my_hash(label)
		if sign == '=':
			is_label_in_box = False if not boxes[box_num] else any(l == label for l, f in boxes[box_num])
			if not is_label_in_box:
				boxes[box_num].append((label, int(focal_length)))
			else:
				boxes[box_num] = [(l, f) if l != label else (l, int(focal_length)) for l, f in boxes[box_num]]
		elif sign == '-':
			boxes[box_num] = [(l, f) for l, f in boxes[box_num] if l != label]

	focusing_power = 0
	for box_num, lenses in boxes.items():
		if len(lenses) != 0:
			focusing_power += sum((box_num + 1) * (idx + 1) * focal_length for idx, (_, focal_length) in enumerate(lenses))

	print(focusing_power)
