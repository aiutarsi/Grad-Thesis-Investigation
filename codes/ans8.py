MAX = 100001


class Queue:
    def __init__(self):
        self.arr = [None for _ in range(MAX)]
        self.head = 0
        self.tail = -1

    def push(self, x):
        if (self.tail + 2) % MAX == self.head:
            return "full"
        self.arr[(self.tail + 1) % MAX] = x
        self.tail = (self.tail + 1) % MAX

    def pop(self):
        if (self.tail + 1) % MAX == self.head:
            return "empty"
        res = self.arr[self.head]
        self.head = (self.head + 1) % MAX
        return res

    def is_empty(self):
        return (self.tail + 1) % MAX == self.head


queue = Queue()

n, q = map(int, input().split())
for i in range(n):
    name, time = input().split()
    queue.push((name, int(time)))

sum = 0
while not queue.is_empty():
    name, time = queue.pop()
    queue.push((name, time - q)) if time > q else print(name, sum + time)
    sum += min(time, q)
