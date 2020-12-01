from itertools import combinations

with open('input_data/01.txt') as f:
    DATA = [x.strip() for x in f.readlines()]

def run_me():
	nums = [int(x) for x in DATA]
	pairings = combinations(nums, 2)
	for pair in pairings:
		if sum(pair) == 2020:
			print(f"Found it! {pair}")
			print(f"Part 1 answer is: {pair[0] * pair[1]}")
			break
	triplets = combinations(nums, 3)
	for triplet in triplets:
		if sum(triplet) == 2020:
			print(f"Found it! {triplet}")
			print(f"Part 2 answer is: {triplet[0] * triplet[1] * triplet[2]}")
			break


if __name__ == "__main__":
	run_me()
