def main(file):
	possible_ids = []

	lines = file.read().splitlines()
	for line in lines:
		game, sets = line.split(': ')
		sets = sets.split('; ')

		impossible = False

		for _set in sets:
			samples = _set.split(', ')
			for sample in samples:
				num_cubes, color = sample.split(' ')
				num_cubes = int(num_cubes)
				if (color == 'red' and num_cubes > 12 or
					color == 'green' and num_cubes > 13 or
					color == 'blue' and num_cubes > 14):
					impossible = True
					break
			if impossible:
				break

		if not impossible:
			possible_ids.append(int(game.split(' ')[1]))

	print(sum(possible_ids))
