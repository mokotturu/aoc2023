import re
import math
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

	roots = [node for node in G.nodes if node.endswith('A')]
	step_count = 0
	reached_end = False
	steps_to_Z = []

	for root in roots:
		while not reached_end:
			children = list(G.successors(root))
			if instructions[step_count % len(instructions)] == 'L':
				root = children[0]
			elif instructions[step_count % len(instructions)] == 'R':
				root = children[1] if len(children) > 1 else children[0]
			step_count += 1
			reached_end = True if root.endswith('Z') else False
		steps_to_Z.append(step_count)
		step_count = 0
		reached_end = False

	print(math.lcm(*steps_to_Z))
