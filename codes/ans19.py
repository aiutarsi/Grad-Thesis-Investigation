BASE = int(1e3 + 7)
DIVISOR = int(1e9 + 7)


def rabin_karp(T, P):
    res = []
    if len(T) < len(P):
        return res

    t_hash = 0
    p_hash = 0
    base_l_power = 1
    for i in range(len(P)):
        t_hash = (t_hash * BASE + ord(T[i])) % DIVISOR
        p_hash = (p_hash * BASE + ord(P[i])) % DIVISOR
        base_l_power = (base_l_power * BASE) % DIVISOR

    if t_hash == p_hash:
        res.append(0)
    for i in range(len(T) - len(P)):
        t_hash = (BASE * t_hash - base_l_power * ord(T[i]) + ord(T[i + len(P)])) % DIVISOR
        if t_hash == p_hash:
            res.append(i + 1)

    return res


T = input()
P = input()

ans = rabin_karp(T, P)
if len(ans):
    print(*ans, sep="\n")
