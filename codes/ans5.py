n = int(input())
G = []
for i in range(n):
    edges = list(map(int, input().split()))
    G.append([]) if edges[1] == 0 else G.append(edges[2:])
    G[i] = [j - 1 for j in G[i]]

d = [-1 for _ in range(n)]
f = [-1 for _ in range(n)]
time = 0


def dfs_sub(cur):
    global time
    d[cur] = time = time + 1
    for nxt in G[cur]:
        if d[nxt] != -1:
            continue
        dfs_sub(nxt)
    f[cur] = time = time + 1


def dfs():
    for i in range(n):
        if d[i] == -1:
            dfs_sub(i)


dfs()

for i in range(n):
    print(i + 1, d[i], f[i])
