# No changes in the match-statement as the command syntax remains the same.
# Only minor changes in the steps executed for each case.
import time


if __name__ == "__main__":
    t_start = time.time()
    x, y, a = 0, 0, 0
    with open("inputs/02.txt") as f:
        for line in f:
            match line.split(" "):
                case ["forward", X]:
                    x += int(X)
                    y += a * int(X)
                case ["down", A]:
                    a += int(A)
                case ["up", A]:
                    a -= int(A)
    print(f"Ans - {x * y}, Time - {(time.time() - t_start) * 1000}ms")
