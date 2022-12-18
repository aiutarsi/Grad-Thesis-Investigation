class SegmentTree:
    def __init__(self, size):
        x = 1
        while size > x:
            x *= 2
        self.n = x
        self.arr = [0 for _ in range(2 * self.n - 1)]

    def set(self, i, x):
        self.arr[i + self.n - 1] = x

    def build(self):
        for i in reversed(range(0, self.n - 1)):
            self.arr[i] = self.arr[2 * i + 1] + self.arr[2 * i + 2]

    def add(self, i, x):
        i += self.n - 1
        self.arr[i] += x
        while i > 0:
            i = (i - 1) // 2
            self.arr[i] = self.arr[2 * i + 1] + self.arr[2 * i + 2]

    def _get_sum_rec(self, x, y, i, cur_l, cur_r):
        if cur_r <= x or y <= cur_l:
            return 0
        elif x <= cur_l and cur_r <= y:
            return self.arr[i]
        else:
            return self._get_sum_rec(x, y, 2 * i + 1, cur_l, (cur_l + cur_r) // 2) + self._get_sum_rec(x, y, 2 * i + 2, (cur_l + cur_r) // 2, cur_r)

    def get_sum(self, x, y):
        return self._get_sum_rec(x, y, 0, 0, self.n)


n, q = map(int, input().split())

tree = SegmentTree(n)

for i in range(q):
    com, x, y = map(int, input().split())
    if com == 0:
        tree.add(x - 1, y)
    else:
        print(tree.get_sum(x - 1, y))
