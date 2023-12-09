def main(file):
	lines = file.read().splitlines()
	sum = 0
	for line in lines:
		values = [int(x) for x in line.split(' ')]
		gaps = [values]

		while True:
			gaps.append([])
			for i in range(1, len(values)):
				gaps[-1].append(values[i] - values[i - 1])
			if all(item == 0 for item in gaps[-1]):
				break
			values = gaps[-1]

		for idx, gap_arr in enumerate(reversed(gaps)):
			if idx == 0:
				gap_arr.append(0)
			else:
				gap_arr.append(gaps[len(gaps) - idx][-1] + gap_arr[-1])

		sum += gaps[0][-1]
	print(sum)
