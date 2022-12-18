MAX = 199


class Stack:
    def __init__(self):
        self.arr = [None for _ in range(MAX)]
        self.head = 0

    def push(self, x):
        if self.head >= MAX:
            return "full"
        self.arr[self.head] = x
        self.head += 1

    def pop(self):
        if self.head == 0:
            return "empty"
        self.head -= 1
        return self.arr[self.head]


stack = Stack()
symbols = input().split()

for symbol in symbols:
    if symbol == "+":
        stack.push(stack.pop() + stack.pop())
    elif symbol == "-":
        stack.push(-(stack.pop() - stack.pop()))
    elif symbol == "*":
        stack.push(stack.pop() * stack.pop())
    else:
        stack.push(int(symbol))

print(stack.pop())
