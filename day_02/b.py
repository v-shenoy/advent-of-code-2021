if __name__ == "__main__":
    x, y, a = 0, 0, 0
    with open("data.txt") as f:
        for line in f:
            match line.split(" "):
                case ["forward", X]:
                    x += int(X)
                    y += a * int(X)
                case ["down", A]:
                    a += int(A)
                case ["up", A]:
                    a -= int(A)
    print(x * y)
