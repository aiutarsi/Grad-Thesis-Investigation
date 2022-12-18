class Node:
    def __init__(self, n):
        self.number = n
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        cur = self.root
        if cur is None:
            self.root = Node(data)
            return
        else:
            while True:
                if data < cur.number:
                    if cur.left is None:
                        cur.left = Node(data)
                        return
                    cur = cur.left
                elif data > cur.number:
                    if cur.right is None:
                        cur.right = Node(data)
                        return
                    cur = cur.right

    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(" " + str(node.number), end="")
            self.in_order(node.right)

    def pre_order(self, node):
        if node is not None:
            print(" " + str(node.number), end="")
            self.pre_order(node.left)
            self.pre_order(node.right)


m = int(input())
tree = BinarySearchTree()

for i in range(m):
    order = input().split()
    if order[0] == "insert":
        tree.insert(int(order[1]))
    else:
        tree.in_order(tree.root)
        print()
        tree.pre_order(tree.root)
        print()
