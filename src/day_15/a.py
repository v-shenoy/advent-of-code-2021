# This is equivalent to the shortest distance problem.
# We solve this using Djikstra's algorithm.
import time
import sys
import heapq


def get_neighbour_indices(n_rows, n_cols, x, y):
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbours = map(lambda p: (p[0] + x, p[1] + y), deltas)

    return filter(lambda p: (0 <= p[0] < n_rows) and (0 <= p[1] < n_cols), neighbours)


def djikstra(cave, n_rows, n_cols):
    dist = [[sys.maxsize] * n_cols for _ in range(n_rows)]
    dist[0][0] = 0
    
    queue = [(dist[0][0], 0, 0)]
    while queue:
        d, i, j = heapq.heappop(queue)

        for (k, l) in get_neighbour_indices(n_rows, n_cols, i, j):
            if d + cave[k][l] < dist[k][l]:
                dist[k][l] = d + cave[k][l]
                heapq.heappush(queue, (dist[k][l], k, l))

    return dist[n_rows - 1][n_cols - 1]


if __name__ == "__main__":
    t_start = time.perf_counter()
    with open("inputs/15.txt") as f:
        cave = [[int(c) for c in line.strip()] for line in f]

    n_rows, n_cols = len(cave), len(cave[0])
    print(f"Ans - {djikstra(cave, n_rows, n_cols)}, Time - {(time.perf_counter() - t_start) * 1000}ms")
