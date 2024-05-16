import numpy as np

def recursive_solve(arrangement, info):
	return 0

def main(file):
	lines = file.read().splitlines()
	total_arrangements = 0
	for line in lines:
		arrangement, info = line.split(' ')
		info = list(map(int, info.split(',')))

		total_arrangements += recursive_solve(arrangement, info)

	print(total_arrangements)