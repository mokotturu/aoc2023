import numpy as np

def main(file):
	lines = file.read().splitlines()

	_, time = lines[0].split(':')
	time = int(''.join([x for x in time.strip() if x != ' ']))

	_, distance = lines[1].split(':')
	distance = int(''.join([x for x in distance.strip() if x != ' ']))

	num_ways = 0
	for _t in range(1, time + 1):
		possible_dist = _t * (time - _t)
		if possible_dist > distance:
			num_ways += 1

	print(num_ways)
