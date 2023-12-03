import math
from collections import defaultdict

def main(file):
	powers = []

	lines = file.read().splitlines()
	for line in lines:
		game, sets = line.split(': ')
		sets = sets.split('; ')

		cubes_collection = defaultdict(list)

		for _set in sets:
			samples = _set.split(', ')
			for sample in samples:
				num_cubes, color = sample.split(' ')
				cubes_collection[color].append(int(num_cubes))

		maxs = [max(cubes_collection[color]) for color in cubes_collection.keys()]
		powers.append(math.prod(maxs))

	print(sum(powers))
