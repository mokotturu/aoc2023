from collections import defaultdict

def main(file):
	idx_to_copy_count = defaultdict(int)

	lines = file.read().splitlines()
	for line_idx, line in enumerate(lines):
		_, info = line.split(': ')
		winning, mine = info.split(' | ')

		winning = winning.split(' ')
		mine = mine.split(' ')

		winning = [int(x) for x in winning if x]
		mine = [int(x) for x in mine if x]

		card_copies = 0
		for num in mine:
			if num in winning:
				card_copies += 1

		idx_to_copy_count[line_idx] += 1
		for copy_card_idx in range(line_idx + 1, line_idx + card_copies + 1):
			idx_to_copy_count[copy_card_idx] += idx_to_copy_count[line_idx]

	print(sum(idx_to_copy_count.values()))
