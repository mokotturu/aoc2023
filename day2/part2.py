import math
from collections import defaultdict

powers = []

while True:
	try:
		line = input()
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
	except EOFError:
		break

print(sum(powers))