if __name__ == "__main__":
    with open("data.txt") as f:
        data = [line.strip() for line in f]
    
    gamma, epsilon = "", ""
    n_rows, n_cols = len(data), len(data[0])

    n_ones_per_col = [sum(int(data[row][col]) for row in range(n_rows)) for col in range(n_cols)]
    
    gamma = "".join(["1" if n_ones > n_rows - n_ones else "0" for n_ones in n_ones_per_col])
    epsilon = "".join(["0" if n_ones > n_rows - n_ones else "1" for n_ones in n_ones_per_col])

    print(int(gamma, 2) * int(epsilon, 2))
