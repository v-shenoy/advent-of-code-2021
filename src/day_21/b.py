# I spent a lot of time on this before realizing I 
# misunderstood the question, and looked it up. 
# This is an elegant solution I found while snooping online.
import time
import itertools
import functools


@functools.lru_cache(maxsize=None)
def play_game(p1, s1, p2, s2):
    w1, w2 = 0, 0
    for dice in itertools.product((1, 2, 3), repeat = 3):
        p1_copy = p1 + sum(dice)
        p1_copy = p1_copy % 10 if p1_copy % 10 else 10
        
        s1_copy = s1 + p1_copy
        if s1_copy >= 21:
            w1 += 1
            continue
        w22, w11 = play_game(p2, s2, p1_copy, s1_copy)
        w1 += w11
        w2 += w22

    return w1, w2


if __name__ == "__main__":
    t_start = time.perf_counter()
    with open("inputs/21.txt") as f:
        p1 = int(f.readline().split(":")[1])
        p2 = int(f.readline().split(":")[1])

    print(f"Ans - {max(play_game(p1, 0, p2, 0))}, Time - {(time.perf_counter() - t_start) * 1000}ms")
