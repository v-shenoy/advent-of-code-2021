import time
from collections import defaultdict


if __name__ == "__main__":
    t_start = time.perf_counter()
    counts = defaultdict(int)
    with open("inputs/05.txt") as f:
        for line in f:
            p1, p2 = line.split("->")
            x1, y1 = map(int, p1.split(","))
            x2, y2 = map(int, p2.split(","))

            x_step = 1 if x2 > x1 else -1
            y_step = 1 if y2 > y1 else -1
            
            if x1 == x2:
                for y in range(y1, y2 + y_step, y_step):
                    counts[(x1, y)] += 1
            elif y1 == y2:
                for x in range(x1, x2 + x_step, x_step):
                    counts[(x, y1)] += 1
            else:
                y = y1
                for x in range(x1, x2 + x_step, x_step):
                    counts[(x, y)] += 1
                    y += y_step

    ans = sum(v >= 2 for v in counts.values())
    print(f"Ans - {ans}, Time - {(time.perf_counter() - t_start) * 1000}ms")
