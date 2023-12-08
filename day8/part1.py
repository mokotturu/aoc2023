import re
import networkx as nx

def main(file):
	lines = file.read().splitlines()
	instructions = list(lines[0])

	G = nx.DiGraph()

	for line in lines[2:]:
		node, children = line.split(' = ')
		children = re.findall(r'\((.+)\)', children)[0].split(', ')
		G.add_node(node)
		for child in children:
			G.add_edge(node, child)

	root = 'AAA'
	step_count = 0
	reached_end = False

	while not reached_end:
		children = list(G.successors(root))
		if instructions[step_count % len(instructions)] == 'L':
			root = children[0]
		elif instructions[step_count % len(instructions)] == 'R':
			root = children[1] if len(children) > 1 else children[0]
		step_count += 1
		reached_end = True if root == 'ZZZ' else False

	print(step_count)
