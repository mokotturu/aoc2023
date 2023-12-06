import numpy as np

def main(file):
	lines = file.read().splitlines()

	_, times = lines[0].split(':')
	times = [int(x) for x in times.strip().split(' ') if x != '']

	_, distances = lines[1].split(':')
	distances = [int(x) for x in distances.strip().split(' ') if x != '']

	total_prod = 1
	for time_idx, time in enumerate(times):
		possible_distances = np.array([_t * (time - _t) for _t in range(1, time + 1)])
		total_prod *= np.sum(possible_distances > distances[time_idx])

	print(total_prod)
