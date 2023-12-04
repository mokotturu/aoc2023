def main(file):
	total_score = 0

	lines = file.read().splitlines()
	for line in lines:
		_, info = line.split(': ')
		winning, mine = info.split(' | ')

		winning = winning.split(' ')
		mine = mine.split(' ')

		winning = [int(x) for x in winning if x]
		mine = [int(x) for x in mine if x]

		score = 0
		for num in mine:
			if num in winning:
				score = 1 if score == 0 else score * 2
		total_score += score

	print(total_score)
