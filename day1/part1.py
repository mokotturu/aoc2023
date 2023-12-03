def main(file):
	nums = []

	lines = file.read().splitlines()
	for line in lines:
		cleaned = ''.join([char for char in line if char.isdigit()])
		nums.append(int(''.join([cleaned[0], cleaned[-1]])))

	print(sum(nums))
