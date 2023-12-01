nums = []

while True:
	try:
		line = input()
		cleaned = ''.join([char for char in line if char.isdigit()])
		nums.append(int(''.join([cleaned[0], cleaned[-1]])))
	except EOFError:
		break

print(sum(nums))