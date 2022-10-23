# For consecutive sliding windows, one might calculate the sum of the three 
# elements in the first window, then calculate the sum of three elements in 
# the next window, and compare them. 
# However, consider a portion of list [... a, b, c, d, ...]
# We can see that a + b + c < b + c + d <==> a < d
# So we need to compare only the fourth element.
import time


if __name__ == "__main__":
    t_start = time.perf_counter()
    with open("inputs/01.txt") as f:
        data = [int(line) for line in f]

    ans = sum(data[i] < data[i+3] for i in range(len(data) - 3))
    print(f"Ans - {ans}, Time - {(time.perf_counter() - t_start) * 1000}ms")
