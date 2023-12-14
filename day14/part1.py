import numpy as np

def main(file):
	grid = np.array([list(line) for line in file.read().splitlines()])

	total = 0
	for col in grid.T:
		rock_map = {}
		round_rock_count = 0
		ceiling = -1
		for cell_idx, cell in enumerate(col):
			if cell == 'O':
				round_rock_count += 1
			if cell == '#' or cell_idx == col.shape[0] - 1:
				rock_map[ceiling] = round_rock_count
				round_rock_count = 0
				ceiling = cell_idx

		top = grid[0].shape[0]
		for key, value in rock_map.items():
			ceiling = top - (key + 1)
			if value != 0:
				total += np.sum(np.arange(ceiling, ceiling - value, -1))

	print(total)
