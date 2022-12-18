def floyd_warshall(G):
    for k in range(len(G)):
        for i in range(len(G)):
            for j in range(len(G)):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])

    for i in range(len(G)):
        if G[i][i] < 0:
            print("NEGATIVE CYCLE")
            return

    G = [["INF" if i == float("inf") else i for i in j] for j in G]
    for i in range(len(G)):
        print(*G[i])


V, E = map(int, input().split())
G = [[float("inf") for _ in range(V)] for _ in range(V)]
for i in range(E):
    s, t, d = map(int, input().split())
    G[s][t] = d
for i in range(V):
    G[i][i] = 0

floyd_warshall(G)
