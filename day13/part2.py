import numpy as np

def check_grid(grid):
	score = 0
	reflection_line_idx = 0
	found_reflection = False
	while reflection_line_idx < grid.shape[0] and not found_reflection:
		num_diffs = 0
		for i in range(min(reflection_line_idx, grid.shape[0] - reflection_line_idx)):
			if not np.array_equal(grid[reflection_line_idx - i - 1, :], grid[reflection_line_idx + i, :]):
				num_diffs += np.sum(grid[reflection_line_idx - i - 1, :] != grid[reflection_line_idx + i, :])
			if num_diffs > 1:
				break
		else:
			if num_diffs == 1:
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
