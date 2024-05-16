import numpy as np

def main(file):
	grid = np.array([list(map(int, list(line))) for line in file.read().splitlines()])
	