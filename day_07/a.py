# Naive way:
# Suppose the min, max frog positions are labelled as leftmost, rightmost respectively.
# The position that minimizes the distance has be in the interval [leftmost, rightmost].
# We iteratve over this interval, and calculate the cost for moving the frogs to each position,
# Number of operations = O((rightmost - leftmost) * n) where n = number of frogs.
# 
# Optimized:
# Suppose the frogs positions are as x_1, x_2, x_3, ..., x_n, where x_1 <= x_2 <= x_3 ... <= x_n
# If we start at position x_k and move r units to the right, such that x_k < x_k + r <= x_k + 1
# we increase the distance from each of x_1, x_2, ... x_k by r-units, 
# and decrease the distances from x_k+1, ... x_n by r-units. The overall cost at 
# x_k+1 changes by k*r - (n - k)*r units.
# We hop along the frog positions, and break if the cost increases. 
# Number of operations = O(n*lgn) [we need to sort the array]
# 
# Standard Lib:
# If we notice that the cost decreases as long as 2*k <= n. We can infer that the minimum
# cost will occur at the median. We can use the standard library to find the median.
# I am unsure if the standard library uses sorting to find the median, or 
# if it uses the median of median algorithm which runs in O(n) time.
# In either cases, it should be faster than method 2 as the standard
# library will leverage C-code.
# It's also a lot cleaner to look at.
import statistics
import time


def naive(data):
    t = time.time()
    leftmost, rightmost = min(data), max(data)
    ans = min(sum(abs(pos - target_pos) for pos in data) for target_pos in range(leftmost, rightmost + 1)) 
    print(f"Naive way:\n\tAns - {ans}, Time - {(time.time() - t) * 1000}ms")


def optimized(data):
    t = time.time()
    data, n = sorted(data), len(data)
    ans = sum(pos - data[0] for pos in data)

    for i in range(1, n):
        disp = data[i] - data[i - 1]
        new_cost = ans + (2*i - n) * disp
        if new_cost > ans:
            break
        ans = new_cost
    print(f"Optimized:\n\tAns - {ans}, Time - {(time.time() - t) * 1000}ms")


def standard_lib(data):
    t = time.time()
    target = statistics.median(data)
    ans = int(sum(abs(pos - target) for pos in data))
    print(f"Standard Lib:\n\tAns - {ans}, Time - {(time.time() - t) * 1000}ms")


if __name__ == "__main__":
    with open("inputs/07.txt") as f:
        data = list(map(int, f.readline().split(","))) 
  
    # naive(data)
    # optimized(data)
    standard_lib(data)
