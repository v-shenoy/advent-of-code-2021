# The initial approach I had was set-theoretic and horribly inefficient. It is in the `old.py` file.
# In this approach, we keep a list of cuboids that are on.
# For any new instruction in a given cuboid range, we calculate its intersection with every previous on cuboid.
# For each,  we split the previously on cuboid into smaller cuboids without the intersection.
# Off and on cuboids are similar, except we add the on cuboids to our list at the end.
# This approach was inspired by reading through day's megathread on r/adventofcode.
# In particular from - https://www.reddit.com/r/adventofcode/comments/rlxhmg/comment/hpv4sjl/?utm_source=share&utm_medium=web2x&context=3
import time
from collections import namedtuple
from typing import Optional


Interval = namedtuple("Interval", ["min", "max"])
Cuboid = namedtuple("Cuboid", ["xs", "ys", "zs"])


def n_points(cuboid: Cuboid) -> int:
    if cuboid is None:
        return 0
    return (cuboid.xs.max - cuboid.xs.min + 1) * (cuboid.ys.max - cuboid.ys.min + 1) * (cuboid.zs.max - cuboid.zs.min + 1)


def get_interval_intersection(i: Interval, u: Interval) -> Optional[Interval]:
    o = Interval(max(i.min, u.min), min(i.max, u.max))

    if o.min <= o.max:
        return o


def get_cuboid_intersection(c1: Cuboid, c2: Cuboid) -> Optional[Cuboid]:
    xs = get_interval_intersection(c1.xs, c2.xs)
    ys = get_interval_intersection(c1.ys, c2.ys)
    zs = get_interval_intersection(c1.zs, c2.zs)

    if xs is not None and ys is not None and zs is not None:
        return Cuboid(xs, ys, zs)


if __name__ == "__main__":
    t_start = time.perf_counter()
    cuboids = []
    with open("inputs/22.txt") as f:
        for line in f:
            turn, cuboid_intervals = line.split()

            turn_on = turn == "on"
            intervals = (Interval(*map(int, interval[2:].split(".."))) for interval in cuboid_intervals.split(","))
            new = Cuboid(*intervals)

            new_cuboids = []
            for old in cuboids:

                cuboids_intersect = all([get_interval_intersection(new.xs, old.xs), get_interval_intersection(new.ys, old.ys), get_interval_intersection(new.zs, old.zs)])
                if not cuboids_intersect:
                    new_cuboids.append(old)
                    continue
        
                # Volume in positive x-direction of new cuboid
                if old.xs.min <= new.xs.max <= old.xs.max: 
                    new_cuboids.append(Cuboid(Interval(new.xs.max + 1, old.xs.max), old.ys, old.zs))
                    old = Cuboid(Interval(old.xs.min, new.xs.max), old.ys, old.zs)
                # Volume in negative x-direction of new cuboid
                if old.xs.min <= new.xs.min <= old.xs.max:
                    new_cuboids.append(Cuboid(Interval(old.xs.min, new.xs.min - 1), old.ys, old.zs))
                    old = Cuboid(Interval(new.xs.min, old.xs.max), old.ys, old.zs)
                # Volume in positive y-direction of new cuboid
                if old.ys.min <= new.ys.max <= old.ys.max: 
                    new_cuboids.append(Cuboid(old.xs, Interval(new.ys.max + 1, old.ys.max), old.zs))
                    old = Cuboid(old.xs, Interval(old.ys.min, new.ys.max), old.zs)
                # Volume in negative y-direction of new cuboid
                if old.ys.min <= new.ys.min <= old.ys.max:
                    new_cuboids.append(Cuboid(old.xs, Interval(old.ys.min, new.ys.min - 1), old.zs))
                    old = Cuboid(old.xs, Interval(new.ys.min, old.ys.max), old.zs)
                # Volume in positive z-direction of new cuboid
                if old.zs.min <= new.zs.max <= old.zs.max: 
                    new_cuboids.append(Cuboid(old.xs, old.ys, Interval(new.zs.max + 1, old.zs.max)))
                    old = Cuboid(old.xs, old.ys, Interval(old.zs.min, new.zs.max))
                # Volume in negative z-direction of new cuboid
                if old.zs.min <= new.zs.min <= old.zs.max:
                    new_cuboids.append(Cuboid(old.xs, old.ys, Interval(old.zs.min, new.zs.min - 1)))
                    old = Cuboid(old.xs, old.ys, Interval(new.zs.min, old.zs.max))

            if turn_on:
                new_cuboids.append(new)

            cuboids = new_cuboids

    target_region = Cuboid(Interval(-50, 50), Interval(-50, 50), Interval(-50, 50))
    ans = sum(map(lambda cuboid: n_points(get_cuboid_intersection(target_region, cuboid)), cuboids))
    print(f"Ans - {ans}, Time - {(time.perf_counter() - t_start) * 1000}ms")
