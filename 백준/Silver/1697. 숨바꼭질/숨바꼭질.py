from collections import deque

n, k = map(int, input().split())

row = [0] * 100_001


def bfs(x):
    q = deque()
    q.append(x)
    row[x] = 1

    while q:
        t = q.popleft()

        n1 = t - 1
        n2 = t + 1
        n3 = t * 2

        if in_boundary(n1) and row[n1] == 0:
            q.append(n1)
            row[n1] = row[t] + 1

        if in_boundary(n2) and row[n2] == 0:
            q.append(n2)
            row[n2] = row[t] + 1

        if in_boundary(n3) and row[n3] == 0:
            q.append(n3)
            row[n3] = row[t] + 1

        if n1 == k or n2 == k or n3 == k:
            return row[k]
        # print(row[0:18:1])
    return -1


def in_boundary(x):
    return 0 <= x <= 100_000


print(bfs(n) - 1)
