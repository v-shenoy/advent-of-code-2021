# Not really sure about the best way. We can't use the median method directly, as the
# cost change is not linear. The solution below  is same as the naive solution in Part A.
# Only difference is that the distance function between two co-ords has changed.
import time


def dist(x, y):
    d = abs(x - y)
    return (d * (d + 1)) // 2


if __name__ == "__main__":
    t = time.time()
    with open("data.txt") as f:
        data = list(map(int, f.readline().split(",")))

    leftmost, rightmost = min(data), max(data)
    ans = min(sum(dist(pos, target_pos) for pos in data) for target_pos in range(leftmost, rightmost + 1))
    print(f"Ans - {ans}, Time - {time.time() - t}s")
