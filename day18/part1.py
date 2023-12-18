import numpy as np

def main(file):
	lines = file.read().splitlines()
	x, y, perimeter, locs = 0, 0, 0, []
	for line in lines:
		dir, dist, color = line.split(' ')
		color = color[1:-1]
		if dir == 'U':
			x -= int(dist)
		elif dir == 'L':
			y -= int(dist)
		elif dir == 'D':
			x += int(dist)
		elif dir == 'R':
			y += int(dist)
		perimeter += int(dist)
		locs.append((x, y))

	xs, ys = zip(*locs)
	area = 0.5 * np.abs(np.dot(xs, np.roll(ys, 1)) - np.dot(ys, np.roll(xs, 1)))
	interior_points = int(area - (perimeter / 2) + 1)
	print(perimeter + interior_points)
