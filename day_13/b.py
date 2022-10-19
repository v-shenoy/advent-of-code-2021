# We simply repeat the procedure for subsequent instructions
# In the final set of points, we find out the max x, y co-ords.
# Using this we print the grid [0, 0] x [x_max, y_max]
# If the point (x, y) is present in the final set, we print
# a "█" (a block character) at the pos (x, y) else we print a " "
# This prints out a readable word which is the answer
import time


def fold(instr, points):
    axis, val = instr.split(" ")[2].split("=")
    is_horizontal_fold, val = (axis == "x"), int(val)

    if is_horizontal_fold:
        return {(2 * val - x, y) if x >= val else (x, y) for (x, y) in points}
    else:
        return {(x, 2 * val - y) if y >= val else (x, y) for (x, y) in points}   


if __name__ == "__main__":
    t_start = time.time()
    
    points = set()
    with open("inputs/13.txt") as f:
        for line in f:
            if line.isspace():
                break
            x, y = map(int, line.split(","))            
            points.add((x, y))
    
        instrs = f.readlines()
    
    for instr in instrs:
        points = fold(instr, points)

    x_max = max(x for (x, _) in points)
    y_max = max(y for (_, y) in points)

    print("Ans - ")
    for y in range(y_max + 1):
        for x in range(x_max + 1):
            c = chr(9608) if (x, y) in points else " "
            print(c, end="")
        print("")
    print(f"Time - {(time.time() - t_start) * 1000}ms")
