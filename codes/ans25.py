from collections import deque


def bfs(G, start):
    dist = [-1 for _ in range(len(G))]
    dist[start] = 0
    queue = deque()
    queue.append(start)

    while queue:
        cur = queue.popleft()
        for nxt in G[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)
    return dist


n = int(input())
G = []
for i in range(n):
    edges = list(map(int, input().split()))
    G.append([]) if edges[1] == 0 else G.append(edges[2:])
    G[i] = [j - 1 for j in G[i]]

ans = bfs(G, 0)
for i in range(n):
    print(i + 1, ans[i])
