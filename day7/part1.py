from collections import Counter

def main(file):
	lines = file.read().splitlines()

	NUM_HANDS = len(lines)
	CARD_ORDER = 'AKQJT98765432'
	hands = {
		(5,): [],
		(1, 4,): [],
		(2, 3,): [],
		(1, 1, 3,): [],
		(1, 2, 2,): [],
		(1, 1, 1, 2,): [],
		(1, 1, 1, 1, 1,): [],
	}

	for line in lines:
		hand, bid = line.strip().split(' ')
		counts = Counter(hand)
		counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1])}
		values = tuple(counts.values())
		hands[values].append((hand, bid))

	highest_rank, amount = NUM_HANDS, 0
	for _, hands_of_type in hands.items():
		if hands_of_type:
			hands_of_type.sort(key=lambda h: [CARD_ORDER.index(char) for char in h[0]])
			for hand in hands_of_type:
				amount += highest_rank * int(hand[1])
				highest_rank -= 1

	print(amount)
