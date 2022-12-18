from collections import deque


def spfa(G, r):
    dist = [float("inf") for _ in range(len(G))]
    queue = deque()
    queue_flag = [False for _ in range(len(G))]
    queue_count = [0 for _ in range(len(G))]

    dist[r] = 0
    queue.append(r)
    queue_flag[r] = True
    queue_count[r] = 1

    while queue:
        cur = queue.pop()
        queue_flag[cur] = False
        for nxt, cost in G[cur]:
            if dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost
                if not queue_flag[nxt]:
                    queue.append(nxt)
                    queue_flag[nxt] = True
                    queue_count[nxt] += 1
                    if queue_count[nxt] >= len(G):
                        print("NEGATIVE CYCLE")
                        return

    for i in range(len(G)):
        print("INF" if dist[i] == float("inf") else dist[i])


V, E, r = map(int, input().split())
G = [[] for _ in range(V)]
for i in range(E):
    s, t, d = map(int, input().split())
    G[s].append((t, d))

spfa(G, r)
