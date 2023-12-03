import argparse
import importlib

if __name__ == '__main__':
	argparser = argparse.ArgumentParser()
	argparser.add_argument('day', type=int, help='day of challenge')
	argparser.add_argument('part', type=int, help='part 1 or 2')
	argparser.add_argument('input', type=str, default='input.txt', help='input file relative to the day\'s folder')
	args = argparser.parse_args()

	with open(f'day{args.day}/{args.input}') as file:
		importlib.import_module(f'day{args.day}.part{args.part}').main(file)
