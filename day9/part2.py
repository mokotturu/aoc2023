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
				gap_arr.insert(0, 0)
			else:
				gap_arr.insert(0, gap_arr[0] - gaps[len(gaps) - idx][0])

		sum += gaps[0][0]
	print(sum)
