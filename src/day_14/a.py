# We keep track of the counter for each letter, as well as the count for each pair.
# At each step, we update the counts using the polymerization rules.
# Suppose we have some pair XY with count c, and a rule XY -> Z
# We increase the count of the pair XZ and ZY by c as they will be created.
# We also increase the count of the letter Z by c.
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
    n_steps = 10
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
