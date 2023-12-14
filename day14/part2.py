import numpy as np

def tilt(grid, dir):
	if dir == 0:
		for col_idx, col in enumerate(grid.T):
			ceiling = -1
			for cell_idx, cell in enumerate(col):
				if cell == 'O':
					ceiling += 1
					grid[cell_idx, col_idx] = '.'
					grid[ceiling, col_idx] = 'O'
				elif cell == '#':
					ceiling = cell_idx
	elif dir == 1:
		for row_idx, row in enumerate(grid):
			ceiling = -1
			for cell_idx, cell in enumerate(row):
				if cell == 'O':
					ceiling += 1
					grid[row_idx, cell_idx] = '.'
					grid[row_idx, ceiling] = 'O'
				elif cell == '#':
					ceiling = cell_idx
	elif dir == 2:
		for col_idx, col in enumerate(grid.T):
			ceiling = col.shape[0]
			for cell_idx, cell in reversed(list(enumerate(col))):
				if cell == 'O':
					ceiling -=1
					grid[cell_idx, col_idx] = '.'
					grid[ceiling, col_idx] = 'O'
				elif cell == '#':
					ceiling = cell_idx
	elif dir == 3:
		for row_idx, row in enumerate(grid):
			ceiling = row.shape[0]
			for cell_idx, cell in reversed(list(enumerate(row))):
				if cell == 'O':
					ceiling -= 1
					grid[row_idx, cell_idx] = '.'
					grid[row_idx, ceiling] = 'O'
				elif cell == '#':
					ceiling = cell_idx
	return grid

def get_load(grid):
	load = 0
	top = grid[0].shape[0]

	for col in grid.T:
		for cell_idx, cell in enumerate(col):
			if cell == 'O':
				load += top - cell_idx
	return load

def main(file):
	grid = np.array([list(line) for line in file.read().splitlines()])

	grid_to_cycle_idx, cycle_idx_to_load = {}, {}
	num_total_cycles = 1_000_000_000
	for cycle_idx in range(1, num_total_cycles):
		for tilt_idx in range(4):
			grid = tilt(grid, tilt_idx)
		str_grid = ''.join(np.ravel(grid))
		if str_grid in grid_to_cycle_idx:
			cycle_start = grid_to_cycle_idx[str_grid]
			cycle_length = cycle_idx - cycle_start
			break
		grid_to_cycle_idx[str_grid] = cycle_idx
		cycle_idx_to_load[cycle_idx] = get_load(grid)

	print(cycle_idx_to_load[cycle_start + ((num_total_cycles - cycle_start) % cycle_length)])
