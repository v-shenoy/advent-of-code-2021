# Calculate the no. of 1's in each column using a list comprehension.
# Another list comprehension to append the most/least common bits to
# gamma, epsilon rates. Parse them as binary integers to calculate the answer.
import time


if __name__ == "__main__":
    t = time.time()
    with open("data.txt") as f:
        data = [line.strip() for line in f]
    
    gamma, epsilon = "", ""
    n_rows, n_cols = len(data), len(data[0])

    n_ones_per_col = [sum(int(data[row][col]) 
        for row in range(n_rows)) 
        for col in range(n_cols)]
    
    gamma = "".join(["1" if n_ones > n_rows - n_ones else "0" 
        for n_ones in n_ones_per_col])
    epsilon = "".join(["0" if n_ones > n_rows - n_ones else "1" 
        for n_ones in n_ones_per_col])

    ans = int(gamma, 2) * int(epsilon, 2)
    print(f"Ans - {ans}, Time - {time.time() - t}s")
