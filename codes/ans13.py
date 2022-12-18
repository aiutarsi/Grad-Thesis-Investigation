class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def _find_root(self, x):
        if x != self.parent[x]:
            self.parent[x] = self._find_root(self.parent[x])
        return self.parent[x]

    def is_same(self, x, y):
        return self._find_root(x) == self._find_root(y)

    def unite(self, x, y):
        root_x = self._find_root(x)
        root_y = self._find_root(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_y] += 1


def kruskal(G, V):
    G.sort(key=lambda x: x[0])
    tree = UnionFind(V)
    ans = 0

    for w, s, t in G:
        if not tree.is_same(s, t):
            ans += w
            tree.unite(s, t)

    return ans


V, E = map(int, input().split())
G = []
for i in range(E):
    s, t, w = map(int, input().split())
    G.append((w, s, t))

print(kruskal(G, V))
