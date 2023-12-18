import numpy as np

def main(file):
	lines = file.read().splitlines()
	x, y, perimeter, locs = 0, 0, 0, []
	for line in lines:
		_, _, color = line.split(' ')
		dir = color[-2]
		dist = int(color[2:-2], base=16)
		if dir == '3':
			x -= int(dist)
		elif dir == '2':
			y -= int(dist)
		elif dir == '1':
			x += int(dist)
		elif dir == '0':
			y += int(dist)
		perimeter += int(dist)
		locs.append((x, y))

	xs, ys = zip(*locs)
	area = 0.5 * np.abs(np.dot(xs, np.roll(ys, 1)) - np.dot(ys, np.roll(xs, 1)))
	interior_points = int(area - (perimeter / 2) + 1)
	print(perimeter + interior_points)
