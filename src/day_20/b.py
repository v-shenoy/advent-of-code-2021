# Only the number of steps change here.
import time
import itertools
import functools


def get_pixel(old_image, n_rows, n_cols, i , j, padding):
    return old_image[i - 1][j - 1] if (1 <= i <= n_rows) and (1 <= j <= n_cols) else padding


def transform_pixel(new_image, old_image, n_rows, n_cols, i, j, algo, padding):
    neighbouring_indices = itertools.product(range(i - 1, i + 2), range(j - 1, j + 2))
    neighbouring_pixels = map(lambda p: get_pixel(old_image, n_rows, n_cols, p[0], p[1], padding), neighbouring_indices)
 
    algo_index = functools.reduce(lambda acc, x: (acc << 1) | x, neighbouring_pixels, 0)
    new_image[i][j] = algo[algo_index]


def enhance(old_image, n_rows, n_cols, algo, padding):
    new_image = [[old_image[i - 1][j - 1] if (1 <= i <= n_rows) and (1 <= j <= n_cols) else 0
        for j in range(n_cols + 2)]
        for i in range(n_rows + 2)]

    for i in range(n_rows + 2):
        for j in range(n_cols + 2):
            transform_pixel(new_image, old_image, n_rows, n_cols, i, j, algo, padding)

    padding = algo[-padding]

    return new_image, n_rows + 2, n_cols + 2, padding


if __name__ == "__main__":
    t_start = time.perf_counter()
    with open("inputs/20.txt") as f:
        algo = [int(c == "#") for c in f.readline().strip()]
        next(f)
        image = [[int(c == "#") for c in line.strip()] for line in f.readlines()]

    n_rows, n_cols, padding = len(image), len(image[0]), 0
    
    n_steps = 50
    while n_steps > 0:
        image, n_rows, n_cols, padding = enhance(image, n_rows, n_cols, algo, padding)
        n_steps -= 1

    ans =  sum(sum(row) for row in image)
    print(f"Ans - {ans}, Time - {(time.perf_counter() - t_start) * 1000}ms")
