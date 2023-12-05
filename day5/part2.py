import numpy as np
from numba import njit, prange
from tqdm import tqdm

def main(file):
	seed_to_soil = []
	soil_to_fertilizer = []
	fertilizer_to_water = []
	water_to_light = []
	light_to_temperature = []
	temperature_to_humidity = []
	humidity_to_location = []

	lines = file.read().splitlines()

	line_idx = 0

	_, seeds_ranges = lines[line_idx].split(': ')
	seeds_ranges = list(map(int, seeds_ranges.split(' ')))
	seeds_ranges = [(seeds_ranges[i], seeds_ranges[i+1]) for i in range(0, len(seeds_ranges), 2)]

	line_idx += 1

	while lines[line_idx] == '':
		line_idx += 1

	line_idx += 1
	while lines[line_idx] != '':
		seed_to_soil.append(list(map(int, lines[line_idx].split(' '))))
		line_idx += 1
	
	line_idx += 2
	while lines[line_idx] != '':
		soil_to_fertilizer.append(list(map(int, lines[line_idx].split(' '))))
		line_idx += 1

	line_idx += 2
	while lines[line_idx] != '':
		fertilizer_to_water.append(list(map(int, lines[line_idx].split(' '))))
		line_idx += 1

	line_idx += 2
	while lines[line_idx] != '':
		water_to_light.append(list(map(int, lines[line_idx].split(' '))))
		line_idx += 1

	line_idx += 2
	while lines[line_idx] != '':
		light_to_temperature.append(list(map(int, lines[line_idx].split(' '))))
		line_idx += 1

	line_idx += 2
	while lines[line_idx] != '':
		temperature_to_humidity.append(list(map(int, lines[line_idx].split(' '))))
		line_idx += 1

	line_idx += 2
	while line_idx < len(lines):
		humidity_to_location.append(list(map(int, lines[line_idx].split(' '))))
		line_idx += 1

	seeds_ranges = np.array(seeds_ranges, dtype=np.int64)
	seed_to_soil = np.array(seed_to_soil, dtype=np.int64)
	soil_to_fertilizer = np.array(soil_to_fertilizer, dtype=np.int64)
	fertilizer_to_water = np.array(fertilizer_to_water, dtype=np.int64)
	water_to_light = np.array(water_to_light, dtype=np.int64)
	light_to_temperature = np.array(light_to_temperature, dtype=np.int64)
	temperature_to_humidity = np.array(temperature_to_humidity, dtype=np.int64)
	humidity_to_location = np.array(humidity_to_location, dtype=np.int64)

	print(find_min(seeds_ranges, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location))

@njit(parallel=True)
def find_min(seeds_ranges, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location):
	min_locations = -1 * np.ones(len(seeds_ranges), dtype=np.int64)
	for seeds_range_idx in prange(len(seeds_ranges)):
		seeds_start, seed_range = seeds_ranges[seeds_range_idx]
		for seed in range(seeds_start, seeds_start + seed_range):
			soil = 0
			for l in seed_to_soil:
				if seed >= l[1] and seed <= l[1] + l[2] - 1:
					soil = l[0] + (seed - l[1])
					break
			else:
				soil = seed

			fertilizer = 0
			for l in soil_to_fertilizer:
				if soil >= l[1] and soil <= l[1] + l[2] - 1:
					fertilizer = l[0] + (soil - l[1])
					break
			else:
				fertilizer = soil

			water = 0
			for l in fertilizer_to_water:
				if fertilizer >= l[1] and fertilizer <= l[1] + l[2] - 1:
					water = l[0] + (fertilizer - l[1])
					break
			else:
				water = fertilizer

			light = 0
			for l in water_to_light:
				if water >= l[1] and water <= l[1] + l[2] - 1:
					light = l[0] + (water - l[1])
					break
			else:
				light = water

			temperature = 0
			for l in light_to_temperature:
				if light >= l[1] and light <= l[1] + l[2] - 1:
					temperature = l[0] + (light - l[1])
					break
			else:
				temperature = light

			humidity = 0
			for l in temperature_to_humidity:
				if temperature >= l[1] and temperature <= l[1] + l[2] - 1:
					humidity = l[0] + (temperature - l[1])
					break
			else:
				humidity = temperature

			location = 0
			for l in humidity_to_location:
				if humidity >= l[1] and humidity <= l[1] + l[2] - 1:
					location = l[0] + (humidity - l[1])
					break
			else:
				location = humidity

			if min_locations[seeds_range_idx] == -1 or location < min_locations[seeds_range_idx]:
				min_locations[seeds_range_idx] = location

	return np.min(min_locations)
