# We keep track of number of fishes with a given timer t, using a dictionary.
# Using this we make the system transition for each day.
# The counts for time t are moved to t - 1, as the timer for the fishes
# decrements. 
# We take note of counts for time 0, as these fishes will give birth after 
# the day. We add the amount of birthed fishes to the timer values for# old
# and new fishes.
import time


if __name__ == "__main__":
    t_start = time.perf_counter()
    with open("inputs/06.txt") as f: 
        data = map(int, f.readline().split(","))
    
    n_days = 80
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

    print(f"Ans - {sum(timers.values())}, Time - {(time.perf_counter() - t_start) * 1000}ms")
