import networkx as nx

def get_neighbors(coord, grid):
	x, y = coord
	neighbors = []
	if grid[y][x] == 'F':
		if x < len(grid[y]) - 1:
			neighbors.append((x + 1, y))
		if y < len(grid) - 1:
			neighbors.append((x, y + 1))
	elif grid[y][x] == '7':
		if x > 0:
			neighbors.append((x - 1, y))
		if y < len(grid) - 1:
			neighbors.append((x, y + 1))
	elif grid[y][x] == 'J':
		if x > 0:
			neighbors.append((x - 1, y))
		if y > 0:
			neighbors.append((x, y - 1))
	elif grid[y][x] == 'L':
		if x < len(grid[y]) - 1:
			neighbors.append((x + 1, y))
		if y > 0:
			neighbors.append((x, y - 1))
	elif grid[y][x] == '|':
		if y > 0:
			neighbors.append((x, y - 1))
		if y < len(grid) - 1:
			neighbors.append((x, y + 1))
	elif grid[y][x] == '-':
		if x > 0:
			neighbors.append((x - 1, y))
		if x < len(grid[y]) - 1:
			neighbors.append((x + 1, y))
	elif grid[y][x] == 'S':
		if x > 0 and grid[y][x - 1] in ['-', 'L', 'F']:
			neighbors.append((x - 1, y))
		if x < len(grid[y]) - 1 and grid[y][x + 1] in ['-', 'J', '7']:
			neighbors.append((x + 1, y))
		if y > 0 and grid[y - 1][x] in ['|', '7', 'F']:
			neighbors.append((x, y - 1))
		if y < len(grid) - 1 and grid[y + 1][x] in ['|', 'L', 'J']:
			neighbors.append((x, y + 1))
	return neighbors

def main(file):
	lines = file.read().splitlines()

	graph = nx.Graph()
	root = None

	for y, line in enumerate(lines):
		x = line.find('S')
		if x != -1:
			root = (x, y)
			break

	last_node, current_node = None, root
	while True:
		neighbors = get_neighbors(current_node, lines)
		next_neighbor = neighbors[0] if neighbors[0] != last_node else neighbors[1]
		graph.add_edge(current_node, next_neighbor)
		last_node, current_node = current_node, next_neighbor
		if current_node == root:
			break

	sssp = nx.single_source_shortest_path_length(graph, root)
	max_value = max(sssp.values())
	print(max_value)
