# Simply iterate through the points and compare value to its neighbour.
import time


def get_neighbour_indices(n_rows, n_cols, x, y):
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbours = map(lambda p: (p[0] + x, p[1] + y), deltas)
    
    return filter(lambda p: (0 <= p[0] < n_rows) and (0 <= p[1] < n_cols), neighbours)


def find_low_points(cave, n_rows, n_cols):
    for x in range(n_rows):
        for y in range(n_cols):
            if all(cave[x][y] < cave[u][v] for u, v in get_neighbour_indices(n_rows, n_cols, x, y)):
                yield x, y


if __name__ == "__main__":
    t = time.time()
    with open("inputs/09.txt") as f:
        cave = [[int(c) for c in line.strip()] for line in f]
    
    n_rows, n_cols = len(cave), len(cave[0])
    ans = sum(1 + cave[x][y] for (x, y) in find_low_points(cave, n_rows, n_cols))
    
    print(f"Ans - {ans}, Time - {time.time() - t}s")
