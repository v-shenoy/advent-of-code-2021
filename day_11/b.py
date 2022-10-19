# Whenever an octopush is flashed, it's energy changes to 0.
# While there are any octopuses with non-zero energy, we keep performing
# transition and flashing octopuses.
import time
import itertools
from itertools import chain


def get_neighbour_indices(n_rows, n_cols, x, y):
    neighbours = itertools.product(range(x - 1, x + 2), range(y - 1, y + 2))
    
    return filter(lambda p: (0 <= p[0] < n_rows) and (0 <= p[1] < n_cols) and not
        (p[0] == x and p[1] == y), neighbours)


def flash(energy, n_rows, n_cols, x, y, flashed):   
    flashed[x][y] = True
    energy[x][y] = 0

    for u, v in get_neighbour_indices(n_rows, n_cols, x, y):
        if not flashed[u][v]:
            energy[u][v] += 1
            if energy[u][v] > 9:
                flash(energy, n_rows, n_cols, u, v, flashed)



if __name__ == "__main__":
    t = time.time()
    with open("inputs/11.txt") as f:
        energy = [[int(c) for c in line.strip()] for line in f]
        
    n_rows, n_cols = len(energy), len(energy[0])
    n_steps = 0

    while any(chain.from_iterable(energy)):
        n_steps += 1
        energy = [[x + 1 for x in row] for row in energy]
        flashed = [[False] * n_cols for _ in range(n_rows)]

        for x in range(n_rows):
            for y in range(n_cols):
                if energy[x][y] > 9:
                    flash(energy, n_rows, n_cols, x, y, flashed)
    print(f"Ans - {n_steps}, Time - {time.time() - t}s")
