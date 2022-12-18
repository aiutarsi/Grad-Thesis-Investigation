class SegmentTree:
    def __init__(self, size):
        x = 1
        while size > x:
            x *= 2
        self.n = x
        self.arr = [float("inf") for _ in range(2 * self.n - 1)]

    def set(self, i, x):
        self.arr[i + self.n - 1] = x

    def build(self):
        for i in reversed(range(0, self.n - 1)):
            self.arr[i] = min(self.arr[2 * i + 1], self.arr[2 * i + 2])

    def update(self, i, x):
        i += self.n - 1
        self.arr[i] = x
        while i > 0:
            i = (i - 1) // 2
            self.arr[i] = min(self.arr[2 * i + 1], self.arr[2 * i + 2])

    def _find_rec(self, x, y, i, cur_l, cur_r):
        if cur_r <= x or y <= cur_l:
            return float("inf")
        elif x <= cur_l and cur_r <= y:
            return self.arr[i]
        else:
            return min(self._find_rec(x, y, 2 * i + 1, cur_l, (cur_l + cur_r) // 2), self._find_rec(x, y, 2 * i + 2, (cur_l + cur_r) // 2, cur_r))

    def find(self, x, y):
        return self._find_rec(x, y, 0, 0, self.n)


n, q = map(int, input().split())

tree = SegmentTree(n)
for i in range(n):
    tree.set(i, 2**31 - 1)
tree.build()

for i in range(q):
    com, x, y = map(int, input().split())
    tree.update(x, y) if com == 0 else print(tree.find(x, y + 1))
