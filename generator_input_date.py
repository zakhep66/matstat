import csv
import random


def generate_unique_random_numbers(count: int, range_nums: int, filename: str) -> None:
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        nums: list = random.sample(range(range_nums), k=count)
        for i in nums:
            writer.writerow([i])
