# While this can be done with a simple if-statement, I think the new
# match-statement introduced in Python 3.10 makes this incredibly clean.
import time


if __name__ == "__main__":
    t = time.time()
    x, y = 0, 0
    with open("inputs/02.txt") as f:
        for line in f:
            match line.split(" "):
                case ["forward", X]:
                    x += int(X)
                case ["down", Y]:
                    y += int(Y)
                case ["up", Y]:
                    y -= int(Y)
    print(f"Ans - {x * y}, Time - {time.time() - t}s")
