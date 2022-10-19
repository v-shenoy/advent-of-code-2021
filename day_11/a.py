# For each step, we perform a transition.
# In a transition, first we increase each Octopus' energy by 1.
# After that we flash any octopuses with energy > 9. This is done using
# a DFS traversal on the matrix for chaining flashes.
import itertools
import time


def get_neighbour_indices(n_rows, n_cols, x, y):
    neighbours = itertools.product(range(x - 1, x + 2), range(y - 1, y + 2))
    
    return filter(lambda p: (0 <= p[0] < n_rows) and (0 <= p[1] < n_cols) and not
        (p[0] == x and p[1] == y), neighbours)


n_flashes = 0
def flash(energy, n_rows, n_cols, x, y, flashed):    
    global n_flashes
    
    flashed[x][y] = True
    energy[x][y] = 0
    
    n_flashes += 1

    for u, v in get_neighbour_indices(n_rows, n_cols, x, y):
        if not flashed[u][v]:
            energy[u][v] += 1
            if energy[u][v] > 9:
                flash(energy, n_rows, n_cols, u, v, flashed)



if __name__ == "__main__":
    t = time.time()
    with open("inputs/11.txt") as f:
        energy = [[int(c) for c in line.strip()] for line in f]
        
    n_steps, ans = 100, {"flashes": 0}
    n_rows, n_cols = len(energy), len(energy[0])

    while n_steps > 0:
        energy = [[x + 1 for x in row] for row in energy]
        flashed = [[False] * n_cols for _ in range(n_rows)]

        for x in range(n_rows):
            for y in range(n_cols):
                if energy[x][y] > 9:
                    flash(energy, n_rows, n_cols, x, y, flashed)
        n_steps -= 1

    print(f"Ans - {n_flashes}, Time - {time.time() - t}s")
