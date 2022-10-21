# I simply go through the lines, and for each point on the line
# increase its count in a dictionary. This makes the runtime 
# dependent on the number of lines, and the co-ordinates of the line.
# But 
# I am sure there must be a way to solve this using geometry, where the
# by calculating the intersections of lines such that the runtime is only
# dependent on the number of lines.
# I simply go through the lines, and for each point on the line
# increase its count in a dictionary. This makes the runtime
# dependent on the number of lines, and the co-ordinates of the line.
#
# But I am sure there must be a way to solve this using geometry, where the
# by calculating the intersections of lines such that the runtime is only
# dependent on the no. of lines.
import time
from collections import defaultdict


if __name__ == "__main__":
    t_start = time.time()
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

    ans = sum(v >= 2 for v in counts.values())
    print(f"Ans - {ans}, Time - {(time.time() - t_start) * 1000}ms")
