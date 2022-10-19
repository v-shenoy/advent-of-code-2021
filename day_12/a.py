# We use a dictionary to store the adjacency lists.
# The problem is solved using a modified recursive-DFS algorithm to count the number of paths.
# In a normal recursive-DFS, whenever we reach a node, we mark it as visited. In this
# case, we only mark lowercase nodes as visited. This allows upper-case nodes to be
# visited more than once.
# Another difference compared to a normal recursive-DFS is that at the end of the DFS-call we
# mark a node as univisited, as it won't be a part of the path anymore.
import time
from collections import defaultdict


ans = 0
def count_paths(graph, curr, visited):
    global ans

    if curr == "end":
        ans += 1
        return

    if curr.islower():
        visited[curr] = True

    for v in graph[curr]:
        if v.isupper() or not visited[v]:
            count_paths(graph, v, visited)

    visited[curr] = False


if __name__ == "__main__":
    t = time.time()
    graph = defaultdict(list)
    with open("inputs/12.txt") as f:
        for line in f:
            u, v = line.strip().split("-")
            graph[u].append(v)
            graph[v].append(u)

    count_paths(graph, "start", defaultdict(bool))
    print(f"Ans - {ans}, Time - {time.time() - t}s")
