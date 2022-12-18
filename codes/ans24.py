from collections import deque


def topological_sort(G, V):
    in_degree = [0 for _ in range(V)]
    out_degree = [[] for _ in range(V)]
    for s, t in G:
        in_degree[t] += 1
        out_degree[s].append(t)

    sorted = []
    queue = deque()
    for index, in_deg in enumerate(in_degree):
        if in_deg == 0:
            sorted.append(index)
            queue.append(index)

    while queue:
        cur = queue.popleft()
        for nxt in out_degree[cur]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                sorted.append(nxt)
                queue.append(nxt)

    return sorted


V, E = map(int, input().split())
G = []
for i in range(E):
    s, t = map(int, input().split())
    G.append((s, t))

print(*topological_sort(G, V), sep="\n")
