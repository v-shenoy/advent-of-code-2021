# Bruteforce.
import time

if __name__ == "__main__":
    t_start = time.time()

    ans = 0
    with open("inputs/08.txt") as f:
        for line in f:
            input, output = line.split("|")[:2]
            break

    print(f"Ans - {ans}, Time - {(time.time() - t_start) * 1000}ms")
