import time


def roll(pos, score, die):
    for _ in range(3):
        pos += die % 10
        pos = pos - 10 if pos > 10 else pos

        die += 1
        die = die - 100 if die > 100 else die

    return pos, score + pos, die


if __name__ == "__main__":
    t_start = time.perf_counter()
    with open("inputs/21.txt") as f:
        p1 = int(f.readline().split(":")[1])
        p2 = int(f.readline().split(":")[1])
    
    s1, s2 = 0, 0
    die, count = 1, 0
    
    ans = 0
    while True:
        p1, s1, die = roll(p1, s1, die)
        count += 3
        if s1 >= 1000:
            ans = s2 * count
            break
        
        p2, s2, die = roll(p2, s2, die)
        count += 3
        if s2 >= 1000:
            ans = s1 * count
            break

    print(f"Ans - {ans}, Time - {(time.perf_counter() - t_start) * 1000}ms")
