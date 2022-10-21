# We use a stack and keep pushing the opening symbols. 
# When we hit a closing symbol, we check the symbol on the stack.
# The string is corrupted, if the symbol on the stack is not
# the corresponding opening symbol
import time


if __name__ == "__main__":
    t_start = time.time()
    opening = ["(", "{", "[", "<"]
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    opening_to_closing = {"(": ")", "[": "]", "{": "}", "<": ">"}
    
    ans = 0
    with open("inputs/10.txt") as f:
        for line in f:
            stack = []
            for c in line.strip():
                if c in opening:
                    stack.append(c)
                elif c != opening_to_closing[stack.pop()]:
                    ans += points[c]
                    break
    
    print(f"Ans - {ans}, Time - {(time.time() - t_start) * 1000}ms")
