# In this case, we are allowed to visit one of the lowercase nodes twice.
# There might be more elegant ways to do this, but I count the paths in two cases.
# Case 1 -
#   In the first case, each lowercase node can be visited at most once in a path.
#   This basically what we computed in the first problem, and I use the same function.
# Case 2 -
#   In this case, we designate one of the lowercase nodes as special (except start or end).
#   And we count the paths where this special node is visited exactly twice. We then
#   to this calculate for every non-terminal lowercase nodes and add them.
#
# Thus the total number of paths is given by
# p(every lower case node is visited at most once) + Σvp(v is visited exactly twice; where v == lowercase, v != start, end)
#
# The reason I had couldn't have a single method where a non-terminal special lowercase node would be visited 0, 1, or 2 times is
# When we call this method while iterating over non-terminal lowercase nodes, we would overcount the paths where every node
# occurs at most once.
# 
# However, this does visit some paths multiple times while computing (we don't count them, but still), so it's not optimal.
import time
from collections import defaultdict


ans = 0
def visit_atmost_once(graph, curr, visited):
    global ans

    if curr == "end":
        ans += 1
        return

    if curr.islower():
        visited[curr] = True

    for v in graph[curr]:
        if v.isupper() or not visited[v]:
            visit_atmost_once(graph, v, visited)

    visited[curr] = False


def visit_exactly_twice(graph, curr, special, count, visited):
    global ans

    if curr == "end":
        if not count:
            ans += 1
        return

    if curr == special:
        count -= 1
    elif curr.islower():
        visited[curr] = True

    for v in graph[curr]:
        if v == special:
            if count:
                visit_exactly_twice(graph, v, special, count, visited)
        elif v.isupper() or not visited[v]:
            visit_exactly_twice(graph, v, special, count, visited)

    if curr == special:
        count += 1
    visited[curr] = False


if __name__ == "__main__":
    t_start = time.perf_counter()
    graph = defaultdict(list)
    with open("inputs/12.txt") as f:
        for line in f:
            u, v = line.strip().split("-")
            graph[u].append(v)
            graph[v].append(u)

    visit_atmost_once(graph, "start", defaultdict(bool))
    for v in filter(lambda v: v.islower() and not (v == "start" or v == "end"), graph):
        visit_exactly_twice(graph, "start", v, 2, defaultdict(bool))
    print(f"Ans - {ans}, Time - {(time.perf_counter() - t_start) * 1000}ms")
