import operator

def filter_for_column(data, n_rows, col, f):
    n_ones = sum(int(data[row][col]) for row in range(n_rows))
    most_common_bit = "1" if n_ones >= n_rows - n_ones else "0"

    return list(filter(lambda num: f(num[col], most_common_bit), data))


if __name__ == "__main__":
    with open("data.txt") as f:
        data = [line.strip() for line in f]

    data_co2 = data.copy()

    col = 0
    while len(data) != 1:
        data = filter_for_column(data, len(data), col, operator.eq)
        col += 1
    o2 = int(data[0], 2)

    col = 0
    while len(data_co2) != 1:
        data_co2 = filter_for_column(data_co2, len(data_co2), col, operator.ne)
        col += 1
    co2 = int(data_co2[0], 2)

    print(o2 * co2)
