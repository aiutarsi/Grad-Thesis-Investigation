def dijkstra(G, r):
    dist = [float("inf") for _ in range(len(G))]
    dist[r] = 0
    done = [False for _ in range(len(G))]

    while True:
        tmp_min_dist = float("inf")
        cur = -1
        for i in range(len(G)):
            if (not done[i]) and (tmp_min_dist > dist[i]):
                tmp_min_dist = dist[i]
                cur = i

        if cur == -1:
            break

        for nxt, cost in G[cur]:
            if dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost

        done[cur] = True

    return dist


n = int(input())
G = [[] for _ in range(n)]
for i in range(n):
    edges = list(map(int, input().split()))
    for j in range(edges[1]):
        G[i].append((edges[2 * j + 2], edges[2 * j + 3]))

ans = dijkstra(G, 0)
for index, cost in enumerate(ans):
    print(index, cost)
