from functools import cache
import numpy as np

def project_beam(grid, num_rows, processed_grid, coords, dir):
	x, y = coords
	energized_tiles = [x * num_rows + y]
	if dir == 0:
		# north
		while x > 0:
			x -= 1
			_processed, _dirs = processed_grid[x * num_rows + y]
			if _processed and dir in _dirs:
				break
			if grid[x * num_rows + y] in '.|':
				_d = _dirs + [_dir_to_add for _dir_to_add in [dir] if _dir_to_add not in _dirs]
				processed_grid[x * num_rows + y] = (True, _d)
				energized_tiles.append(x * num_rows + y)
			elif grid[x * num_rows + y] == '-':
				_d = _dirs + [_dir_to_add for _dir_to_add in [1, 3] if _dir_to_add not in _dirs]
				processed_grid[x * num_rows + y] = (True, _d)
				energized_tiles += project_beam(grid, num_rows, processed_grid, (x, y), 1) + project_beam(grid, num_rows, processed_grid, (x, y), 3)
			elif grid[x * num_rows + y] == '\\':
				_d = _dirs + [_dir_to_add for _dir_to_add in [1] if _dir_to_add not in _dirs]
				processed_grid[x * num_rows + y] = (True, _d)
				energized_tiles += project_beam(grid, num_rows, processed_grid, (x, y), 1)
			elif grid[x * num_rows + y] == '/':
				_d = _dirs + [_dir_to_add for _dir_to_add in [3] if _dir_to_add not in _dirs]
				processed_grid[x * num_rows + y] = (True, _d)
				energized_tiles += project_beam(grid, num_rows, processed_grid, (x, y), 3)
	elif dir == 1:
		# west
		while y > 0:
			y -= 1
			_processed, _dirs = processed_grid[x * num_rows + y]
			if _processed and dir in _dirs:
				break
			if grid[x * num_rows + y] in '.-':
				_d = _dirs + [_dir_to_add for _dir_to_add in [dir] if _dir_to_add not in _dirs]
				processed_grid[x * num_rows + y] = (True, _d)
				energized_tiles.append(x * num_rows + y)
			elif grid[x * num_rows + y] == '|':
				_d = _dirs + [_dir_to_add for _dir_to_add in [0, 2] if _dir_to_add not in _dirs]
				processed_grid[x * num_rows + y] = (True, _d)
				energized_tiles += project_beam(grid, num_rows, processed_grid, (x, y), 0) + project_beam(grid, num_rows, processed_grid, (x, y), 2)
			elif grid[x * num_rows + y] == '\\':
				_d = _dirs + [_dir_to_add for _dir_to_add in [0] if _dir_to_add not in _dirs]
				processed_grid[x * num_rows + y] = (True, _d)
				energized_tiles += project_beam(grid, num_rows, processed_grid, (x, y), 0)
			elif grid[x * num_rows + y] == '/':
				_d = _dirs + [_dir_to_add for _dir_to_add in [2] if _dir_to_add not in _dirs]
				processed_grid[x * num_rows + y] = (True, _d)
				energized_tiles += project_beam(grid, num_rows, processed_grid, (x, y), 2)
	elif dir == 2:
		# south
		while x < num_rows - 1:
			x += 1
			_processed, _dirs = processed_grid[x * num_rows + y]
			if _processed and dir in _dirs:
				break
			if grid[x * num_rows + y] in '.|':
				_d = _dirs + [_dir_to_add for _dir_to_add in [dir] if _dir_to_add not in _dirs]
				processed_grid[x * num_rows + y] = (True, _d)
				energized_tiles.append(x * num_rows + y)
			elif grid[x * num_rows + y] == '-':
				_d = _dirs + [_dir_to_add for _dir_to_add in [1, 3] if _dir_to_add not in _dirs]
				processed_grid[x * num_rows + y] = (True, _d)
				energized_tiles += project_beam(grid, num_rows, processed_grid, (x, y), 1) + project_beam(grid, num_rows, processed_grid, (x, y), 3)
			elif grid[x * num_rows + y] == '\\':
				_d = _dirs + [_dir_to_add for _dir_to_add in [3] if _dir_to_add not in _dirs]
				processed_grid[x * num_rows + y] = (True, _d)
				energized_tiles += project_beam(grid, num_rows, processed_grid, (x, y), 3)
			elif grid[x * num_rows + y] == '/':
				_d = _dirs + [_dir_to_add for _dir_to_add in [1] if _dir_to_add not in _dirs]
				processed_grid[x * num_rows + y] = (True, _d)
				energized_tiles += project_beam(grid, num_rows, processed_grid, (x, y), 1)
	elif dir == 3:
		# east
		while y < len(grid) // num_rows - 1:
			y += 1
			_processed, _dirs = processed_grid[x * num_rows + y]
			if _processed and dir in _dirs:
				break
			if grid[x * num_rows + y] in '.-':
				_d = _dirs + [_dir_to_add for _dir_to_add in [dir] if _dir_to_add not in _dirs]
				processed_grid[x * num_rows + y] = (True, _d)
				energized_tiles.append(x * num_rows + y)
			elif grid[x * num_rows + y] == '|':
				_d = _dirs + [_dir_to_add for _dir_to_add in [0, 2] if _dir_to_add not in _dirs]
				processed_grid[x * num_rows + y] = (True, _d)
				energized_tiles += project_beam(grid, num_rows, processed_grid, (x, y), 0) + project_beam(grid, num_rows, processed_grid, (x, y), 2)
			elif grid[x * num_rows + y] == '\\':
				_d = _dirs + [_dir_to_add for _dir_to_add in [2] if _dir_to_add not in _dirs]
				processed_grid[x * num_rows + y] = (True, _d)
				energized_tiles += project_beam(grid, num_rows, processed_grid, (x, y), 2)
			elif grid[x * num_rows + y] == '/':
				_d = _dirs + [_dir_to_add for _dir_to_add in [0] if _dir_to_add not in _dirs]
				processed_grid[x * num_rows + y] = (True, _d)
				energized_tiles += project_beam(grid, num_rows, processed_grid, (x, y), 0)
	return energized_tiles

def main(file):
	lines = file.read().splitlines()
	grid = ''.join(lines)
	num_rows = len(lines)
	num_cols = len(lines[0])
	processed_grid = [(False, []) for x in range(num_rows) for y in range(num_cols)]
	processed_grid[0 * num_rows + 0] = (True, [3])
	energized_tiles = project_beam(grid, num_rows, processed_grid, (0, 0), 3)
	energized_tiles = list(set(energized_tiles))
	print(len(energized_tiles))
	# new_grid = np.array(list(grid)).reshape(num_rows, num_cols)
	# for x in range(num_rows):
	# 	for y in range(num_cols):
	# 		if (x, y) in energized_tiles:
	# 			new_grid[x, y] = '#'
	# 		else:
	# 			new_grid[x, y] = '.'

	# print(new_grid)