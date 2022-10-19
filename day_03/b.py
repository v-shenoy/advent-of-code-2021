# The filter_for_column filters the bit-strings based on the most/least common
# bit in a particular column. We pass in a function to determine which 
# one we want to select for the O2, CO2 rates resp.
# This method is then continuously called on the list of bit-strings,
# with increasing column index, until only one remains.
import operator
import time


def filter_for_column(data, n_rows, col, f):
    n_ones = sum(int(data[row][col]) for row in range(n_rows))
    most_common_bit = "1" if n_ones >= n_rows - n_ones else "0"

    return list(filter(lambda num: f(num[col], most_common_bit), data))


if __name__ == "__main__":
    t = time.time()
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

    print(f"Ans - {o2 * co2}, Time - {time.time() - t}s")
