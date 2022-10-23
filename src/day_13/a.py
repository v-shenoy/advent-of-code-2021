# Support we are folding at the X = k line (i.e folding left)
# Consider a point (x, y) left of this line (x < k). When we folder the paper
# towards the left at the X = k line, this point does not move.
# Now consider a point (x, y) to right of the line (x >= k). This point is at 
# a distance of x - k from the line. After folding this point has to be the
# same distance from the boundary. So it's new x co-ordinate x' + x - k = k
# Therefore, x' = 2k - x.
# Thus when we fold towards left at the X = k line the points get 
# mapped to (2k - x, y) for x >= k and (x, y) for x < k.
# Likewise when we fold up, the point (x, y) getss mapped to
# (x, 2k - y) for y >= k and (x, y) for y < k.
import time


def fold(instr, points):
    axis, k = instr.split(" ")[2].split("=")
    k = int(k)

    if axis == "x":
        return {(2 * k - x, y) if x >= k else (x, y) for (x, y) in points}
    else:
        return {(x, 2 * k - y) if y >= k else (x, y) for (x, y) in points}   


if __name__ == "__main__":
    t_start = time.perf_counter()
    
    points = set()
    with open("inputs/13.txt") as f:
        for line in f:
            if line.isspace():
                break
            x, y = map(int, line.split(","))            
            points.add((x, y))
    
        instr = f.readline()
    
    points = fold(instr, points)
    print(f"Ans - {len(points)}, Time - {(time.perf_counter() - t_start) * 1000}ms")
