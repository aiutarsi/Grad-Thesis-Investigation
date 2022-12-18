MAX = 10000
hash = [-1 for _ in range(MAX)]


def insert(x):
    hashed_x = x % MAX
    for i in range(MAX):
        index = (hashed_x + i) % MAX
        if hash[index] == -1:
            hash[index] = x
            break


def search(x):
    hashed_x = x % MAX
    for i in range(MAX):
        index = (hashed_x + i) % MAX
        if hash[index] == -1:
            return False
        elif hash[index] == x:
            return True
    return False


n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

for s in S:
    insert(s)
ans = 0
for t in T:
    if search(t):
        ans += 1

print(ans)
