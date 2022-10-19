# Literally no change from part A, except n_days.
import time


if __name__ == "__main__":
    time_start = time.time()
    with open("inputs/06.txt") as f: 
        data = map(int, f.readline().split(","))
    
    n_days = 256
    reset_timer, new_timer = 6, 8
    timers = {t: 0 for t in range(new_timer + 1)}
    for t in data:
        timers[t] += 1

    while n_days > 0:
        new_fishes = timers[0]
        
        timers = {t - 1: timers[t] for t in range(1, new_timer + 1)}
        
        timers[reset_timer] += new_fishes
        timers[new_timer] = new_fishes
        
        n_days -= 1

    print(f"Ans - {sum(timers.values())}, Time - {time.time() - time_start}s")
