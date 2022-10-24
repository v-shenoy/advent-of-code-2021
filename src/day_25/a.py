import re
import time
import copy


def move_right(region, n_rows, n_cols):
    new_region = [["."] * n_cols for _ in range(n_rows)]
    
    has_moved_right = False
    for i in range(n_rows):
        for j in range(n_cols):
            if region[i][j] == ".":
                continue
            elif region[i][j] == ">" and region[i][(j + 1) % n_cols] == ".":
                new_region[i][(j + 1) % n_cols] = ">"
                has_moved_right = True
            else:
                new_region[i][j] = region[i][j]
    
    return new_region, has_moved_right


def move_down(region, n_rows, n_cols):
    new_region = [["."] * n_cols for _ in range(n_rows)]
    
    has_moved_down = False
    for i in range(n_rows):
        for j in range(n_cols):
            if region[i][j] == ".":
                continue
            elif region[i][j] == "v" and region[(i + 1) % n_rows][j] == ".":
                new_region[(i + 1) % n_rows][j] = "v"
                has_moved_down = True
            else:
                new_region[i][j] = region[i][j]
    
    return new_region, has_moved_down


if __name__ == "__main__":
    t_start = time.perf_counter()
    with open("inputs/25.txt") as f:
        region = [list(line.strip()) for line in f]

    n_rows, n_cols = len(region), len(region[0])
    ans = 0
    while True:
        ans += 1
        region, has_moved_right = move_right(region, n_rows, n_cols)
        region, has_moved_down = move_down(region, n_rows, n_cols)
            
        if not (has_moved_right or has_moved_down):
            break

    print(f"Ans - {ans}, Time - {(time.perf_counter() - t_start) * 1000}ms")
