import networkx as nx

def main(file):
	lines = file.read().splitlines()

	graph = nx.Graph()
	root = None

	dim = len(lines)

	for y, line in enumerate(lines):
		for x, char in enumerate(line):
			# south and east
			if char == 'F':
				if (x < dim - 1 and lines[y][x + 1] in ['S', '-', 'J', '7']
				and y < dim - 1 and lines[y + 1][x] in ['S', '|', 'J', 'L']):
					graph.add_edge((x, y), (x + 1, y))
					graph.add_edge((x, y), (x, y + 1))
			# south and west
			elif char == '7':
				if (x > 0 and lines[y][x - 1] in ['S', '-', 'L', 'F']
				and y < dim - 1 and lines[y + 1][x] in ['S', '|', 'L', 'J']):
					graph.add_edge((x, y), (x - 1, y))
					graph.add_edge((x, y), (x, y + 1))
			# north and west
			elif char == 'J':
				if (x > 0 and lines[y][x - 1] in ['S', '-', 'L', 'F']
				and y > 0 and lines[y - 1][x] in ['S', '|', '7', 'F']):
					graph.add_edge((x, y), (x - 1, y))
					graph.add_edge((x, y), (x, y - 1))
			# north and east
			elif char == 'L':
				if (x < dim - 1 and lines[y][x + 1] in ['S', '-', 'J', '7']
				and y > 0 and lines[y - 1][x] in ['S', '|', '7', 'F']):
					graph.add_edge((x, y), (x + 1, y))
					graph.add_edge((x, y), (x, y - 1))
			# north and south
			elif char == '|':
				if (y > 0 and lines[y - 1][x] in ['S', '|', '7', 'F']
				and y < dim - 1 and lines[y + 1][x] in ['S', '|', 'L', 'J']):
					graph.add_edge((x, y), (x, y - 1))
					graph.add_edge((x, y), (x, y + 1))
			# east and west
			elif char == '-':
				if (x > 0 and lines[y][x - 1] in ['S', '-', 'L', 'F']
				and x < dim - 1 and lines[y][x + 1] in ['S', '-', 'J', '7']):
					graph.add_edge((x, y), (x - 1, y))
					graph.add_edge((x, y), (x + 1, y))
			# root
			elif char == 'S':
				root = (x, y)

	sssp = nx.single_source_shortest_path_length(graph, root)
	max_value = max(sssp.values())
	print(max_value)
