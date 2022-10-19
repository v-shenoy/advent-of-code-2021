# Iterate over the numbers, while comparing adjacent elements.
# Some Pythonic list magic to make it look clean.
import time


if __name__ == "__main__":
    t = time.time()
    with open("data.txt") as f:
        data = [int(line) for line in f]

    ans = sum(data[i] < data[i+1] for i in range(len(data) - 1))
    print(f"Ans - {ans}, Time - {time.time() - t}s")
