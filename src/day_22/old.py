# The initial approach that I took to solve this problem was set-theoretic.
# n(A or B) = n(A) + n(B) - n(A and B)
# n(A or B or C) = n(A) + n(B) + n(C) - n(A and B) - n (A and C) - n (B and C) + n(A and B and C)
# and so on ...
# We go through each instruction. We calculate the intersection of the cuboidal
# region with the previous cuboids. Each cuboid has a sign whether it is to be added,
# or removed from the union sum ^ in the above math formulas.
# We add the intersection area with the flipped sign.
# We do this for both turn on and off instruction, the only difference is for on instructions
# we add the cuboid itself to the list.
# This is inefficient because for n sets there are 2^n - 1 elements in the sum.
# So the ith instruction will take time proportional to 2^i - 1.
# The overall of running time of the program is be exponential.
import time
from typing import  Tuple, NamedTuple, Optional


def get_intersection(I: Tuple[int, int], U: Tuple[int, int]) -> Optional[Tuple[int, int]]:
    intersection = (max(I[0], U[0]), min(I[1], U[1]))

    if intersection[0] <= intersection[1]:
        return intersection


class Cuboid(NamedTuple):
    xs: Tuple[int, int]
    ys: Tuple[int, int]
    zs: Tuple[int, int]
    sign: bool

    def n_points(self):
        return (self.xs[1] - self.xs[0] + 1) * (self.ys[1] - self.ys[0] + 1) * (self.zs[1] - self.zs[0] + 1)

    def __and__(self, other: "Cuboid"):
        xs = get_intersection(self.xs, other.xs)
        ys = get_intersection(self.ys, other.ys)
        zs = get_intersection(self.zs, other.zs)

        if xs is not None and ys is not None and zs is not None:
            return Cuboid(xs, ys, zs, -other.sign)


if __name__ == "__main__":
    t_start = time.perf_counter()
    cuboids = []
    with open("inputs/22.txt") as f:
        for line in f:
            flip, cuboid = line.split()

            flip = flip == "on"
            intervals = (tuple(int(i) 
                for i in interval[2:].split("..")) 
                for interval in cuboid.split(","))
            cuboid = Cuboid(*intervals, 1)
            
            new_cuboids = []
            
            for other_cuboid in cuboids:
                new_cuboids.append(other_cuboid)
                
                intersection = cuboid & other_cuboid
                if intersection is not None:
                    new_cuboids.append(intersection)

            if flip:
                new_cuboids.append(cuboid)
            cuboids = new_cuboids

    ans = 0
    for cuboid in cuboids:
        ans += cuboid.sign * cuboid.n_points()

    print(f"Ans - {ans}, Time - {(time.perf_counter() - t_start) * 1000}ms")
