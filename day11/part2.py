from itertools import combinations
import numpy as np

def main(file):
	lines = file.read().splitlines()
	skipped_rows = [row_idx for row_idx in range(len(lines)) if all(cell == '.' for cell in lines[row_idx])]
	skipped_cols = [col_idx for col_idx in range(len(lines[0])) if all(line[col_idx] == '.' for line in lines)]

	grid = np.array([[cell == '#' for cell in line] for line in lines], dtype=bool)
	galaxies = [(x, y) for x, y in np.argwhere(grid)]
	galaxy_pairs = np.array(list(combinations(galaxies, 2)))

	sum_distances = 0
	for (x0, y0), (x1, y1) in galaxy_pairs:
		lower_x, upper_x = min(x0, x1), max(x0, x1)
		lower_y, upper_y = min(y0, y1), max(y0, y1)
		gaps_in_x = len([row_idx for row_idx in skipped_rows if lower_x < row_idx < upper_x])
		gaps_in_y = len([col_idx for col_idx in skipped_cols if lower_y < col_idx < upper_y])
		sum_distances += np.abs(x0 - x1) + np.abs(y0 - y1) + (gaps_in_x + gaps_in_y) * 999999

	print(sum_distances)
