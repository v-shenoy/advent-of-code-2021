# Only difference between part A & B is the number of steps.
import time
from collections import Counter


if __name__ == "__main__":
    t_start = time.perf_counter()
    rules = {}
    with open("inputs/14.txt") as f:
        polymer = f.readline().strip()
        next(f)
        for line in f:
            pair, output = line.split("->")
            rules[pair.strip()] = output.strip()

    letter_counter = Counter(polymer)
    pair_counter = Counter("".join([x, y]) for x, y in zip(polymer, polymer[1:]))
    n_steps = 40
    while n_steps > 0:
        new_pair_counter = Counter()
        for pair, middle_char in rules.items():
            count = pair_counter[pair]
            new_pair_counter[pair[0] + middle_char] += count
            new_pair_counter[middle_char + pair[1]] += count

            letter_counter[middle_char] += count
        pair_counter = new_pair_counter
        n_steps -= 1

    most_common = letter_counter.most_common()[0][1]
    least_common = letter_counter.most_common()[-1][1]
    print(f"Ans - {most_common - least_common}, Time - {(time.perf_counter() - t_start) * 1000}ms")
