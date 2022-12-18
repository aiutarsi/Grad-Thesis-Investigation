def bellman_ford(G, V, r):
    dist = [float("inf") for _ in range(V)]
    dist[r] = 0

    for i in range(V):
        for s, t, d in G:
            if dist[t] > dist[s] + d:
                dist[t] = dist[s] + d
                if i == V - 1:
                    print("NEGATIVE CYCLE")
                    return

    for i in range(V):
        print("INF" if dist[i] == float("inf") else dist[i])


V, E, r = map(int, input().split())
G = []
for i in range(E):
    s, t, d = map(int, input().split())
    G.append((s, t, d))

bellman_ford(G, V, r)
