if __name__ == "__main__":
    x, y = 0, 0
    with open("data.txt") as f:
        for line in f:
            match line.split(" "):
                case ["forward", X]:
                    x += int(X)
                case ["down", Y]:
                    y += int(Y)
                case ["up", Y]:
                    y -= int(Y)
    print(x * y)
