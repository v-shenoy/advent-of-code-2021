if __name__ == "__main__":
    with open("data.txt") as f:
        data = [int(line) for line in f]

    ans = sum(data[i] < data[i+3] for i in range(len(data) - 3))
    print(ans)
