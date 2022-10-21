# No change to the algorithm. We just need to construct
# the bigger cave and run Djikstra on it, instead of 
# running it directly on the input.
import time
import sys
import heapq


def get_neighbour_indices(n_rows, n_cols, i, j):
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbours = map(lambda p: (p[0] + i, p[1] + j), deltas)
    
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


def construct_big_cave(cave, n_rows, n_cols):
    big_cave = []
    for i in range(5 * n_rows): 
        row = []
        for j in range(5 * n_cols):
            new_val = cave[i % n_rows][j % n_cols] + i // n_rows + j // n_cols
            row.append(new_val - 9 if new_val > 9 else new_val)
        big_cave.append(row)
    return big_cave, 5 * n_rows, 5 * n_cols


if __name__ == "__main__":
    t_start = time.time()
    with open("inputs/15.txt") as f:
        cave = [[int(c) for c in line.strip()] for line in f]
    
    
    n_rows, n_cols = len(cave), len(cave[0])
    cave, n_rows, n_cols = construct_big_cave(cave, n_rows, n_cols)
    print(f"Ans - {djikstra(cave, n_rows, n_cols)}, Time - {(time.time() - t_start) * 1000}ms")
