# Use solution from part A to find the low points of the cave.
# Perform DFS with each low point as source and count number of visited points.
# Sort the list of basin sizes to taken product of the largest 3.
import time
from math import prod


def get_neighbour_indices(n_rows, n_cols, x, y):
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbours = map(lambda p: (p[0] + x, p[1] + y), deltas)
    
    return filter(lambda p: (0 <= p[0] < n_rows) and (0 <= p[1] < n_cols), neighbours)


def find_low_points(cave, n_rows, n_cols):
    for x in range(n_rows):
        for y in range(n_cols):
            if all(cave[x][y] < cave[u][v] for u, v in get_neighbour_indices(n_rows, n_cols, x, y)):
                yield x, y


def find_basins(cave, n_rows, n_cols, x, y, visited):   
    stack = [(x, y)]
    ans = 0

    while stack:
        x, y = stack.pop()
        visited[x][y] = True    
        ans += 1

        for u, v in get_neighbour_indices(n_rows, n_cols, x, y):
            if not visited[u][v] and cave[u][v] != 9:
                stack.append((u, v))
                visited[u][v] = True

    return ans


if __name__ == "__main__":
    t = time.time()
    with open("inputs/09.txt") as f:
        cave = [[int(c) for c in line.strip()] for line in f]
    
    n_rows, n_cols = len(cave), len(cave[0])
    visited = [[False] * n_cols for _ in range(n_rows)]
    basins = sorted(find_basins(cave, n_rows, n_cols, x, y, visited) 
        for x, y in find_low_points(cave, n_rows, n_cols))
    
    ans = prod(basins[-3:])
    print(f"Ans - {ans}, Time - {time.time() - t}s")
