# To determine the output on the 4-digit display, for part A
# we do not need to infer from the input signals. 
# The digits 1, 4, 7, 8 have unique number of segments on 
# the 7-segment display and we can identify them directly on
# the right hand side.
import time


if __name__ == "__main__":
    t_start = time.time()
    
    ans = 0
    unique_lens ={2, 4, 3, 7}
    with open("inputs/08.txt") as f:
        for line in f:
            output = line.split("|")[1]
            ans += sum((len(digit) in unique_lens) for digit in output.split())

    print(f"Ans - {ans}, Time - {(time.time() - t_start) * 1000}ms")
