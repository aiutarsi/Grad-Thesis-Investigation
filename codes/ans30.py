import heapq


def dijkstra(G, r):
    dist = [float("inf") for _ in range(len(G))]
    dist[r] = 0
    queue = []
    heapq.heapify(queue)
    heapq.heappush(queue, (dist[r], r))

    while queue:
        cur_dist, cur = heapq.heappop(queue)
        for nxt, cost in G[cur]:
            if dist[nxt] > cur_dist + cost:
                dist[nxt] = cur_dist + cost
                heapq.heappush(queue, (dist[nxt], nxt))

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
