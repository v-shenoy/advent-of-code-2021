if __name__ == "__main__":
    with open("data.txt") as f:
        data = [int(line) for line in f]

    ans = sum(data[i] < data[i+1] for i in range(len(data) - 1))
    print(ans)
