nums = []
CONST_NUMS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

while True:
	try:
		line = input()
		buf = ''
		first_dig, second_dig = None, None
		found_second = False
		for char in line:
			if char.isdigit():
				first_dig = int(char)
				break
			else:
				buf += char
				for _cn in CONST_NUMS:
					if buf.endswith(_cn):
						first_dig = CONST_NUMS.index(_cn) + 1
						found_second = True
						break
				if found_second:
					break

		found_second = False
		buf = ''
		for char in reversed(line):
			if char.isdigit():
				second_dig = int(char)
				break
			else:
				buf = char + buf
				for _cn in CONST_NUMS:
					if buf.startswith(_cn):
						second_dig = CONST_NUMS.index(_cn) + 1
						found_second = True
						break
				if found_second:
					break
		nums.append(int(''.join([str(first_dig), str(second_dig)])))
	except EOFError:
		break

print(sum(nums))