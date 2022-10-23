# We perform the same steps used for checking corruption.
# Once we know that the string is not corrupted, we start
# popping off the stack and adding the corresponding closing brace.
# We put these in a list and take the median.
import time
import statistics


if __name__ == "__main__":
    t_start = time.perf_counter()
    opening = ["(", "{", "[", "<"]
    points = {")": 1, "]": 2, "}": 3, ">": 4}
    opening_to_closing = {"(": ")", "[": "]", "{": "}", "<": ">"}
    
    scores = []
    with open("inputs/10.txt") as f:
        for line in f:
            stack = []
            ans = 0
            is_corrupted = False
            for c in line.strip():
                if c in opening:
                    stack.append(c)
                elif c != opening_to_closing[stack.pop()]:
                    is_corrupted = True
                    break
        
            if not is_corrupted:
                while stack:
                    ans = 5 * ans + points[opening_to_closing[stack.pop()]]
                scores.append(ans)

    print(f"Ans - {statistics.median(scores)}, Time - {(time.perf_counter() - t_start) * 1000}ms")
