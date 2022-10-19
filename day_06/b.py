from cgitb import reset
from collections import defaultdict

if __name__ == "__main__":
    with open("data.txt") as f: 
        data = map(int, f.readline().split(","))
    
    n_days = 256
    reset_timer, new_timer = 6, 8
    fish_counts = {timer: 0 for timer in range(new_timer + 1)}
    for timer in data:
        fish_counts[timer] += 1

    while n_days > 0:
        new_fishes = fish_counts[0]
        fish_counts = {timer - 1: fish_counts[timer] for timer in range(1, new_timer + 1)}
        fish_counts[reset_timer] += new_fishes
        fish_counts[new_timer] = new_fishes
        
        n_days -= 1

    print(sum(fish_counts.values()))
