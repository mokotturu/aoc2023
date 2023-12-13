import numpy as np

def check_grid(grid):
	score = 0
	reflection_line_idx = 0
	found_reflection = False
	while reflection_line_idx < grid.shape[0] and not found_reflection:
		reflecting_so_far = False
		for i in range(min(reflection_line_idx, grid.shape[0] - reflection_line_idx)):
			if not np.array_equal(grid[reflection_line_idx - i - 1, :], grid[reflection_line_idx + i, :]):
				break
			reflecting_so_far = True
		else:
			if reflecting_so_far:
				found_reflection = True
				score += reflection_line_idx
		reflection_line_idx += 1
	return score, found_reflection

def main(file):
	grids = [np.array([list(line) for line in grid.splitlines()]) for grid in file.read().split('\n\n')]

	total = 0
	for grid in grids:
		score, found_reflection = check_grid(grid)
		total += score * 100

		if found_reflection:
			continue

		grid = grid.T
		score, found_reflection = check_grid(grid)
		total += score

	print(total)
