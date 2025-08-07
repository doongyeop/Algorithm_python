from collections import deque

def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

t = int(input())

for _ in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    stores = [tuple(map(int, input().split())) for _ in range(n)]
    rx, ry = map(int, input().split())

    visited = [False] * n
    q = deque()
    q.append((hx, hy))

    possible = False

    while q:
        x, y = q.popleft()

        if manhattan(x, y, rx, ry) <= 1000:
            possible = True
            break

        for i in range(n):
            if not visited[i]:
                sx, sy = stores[i]
                if manhattan(x, y, sx, sy) <= 1000:
                    visited[i] = True
                    q.append((sx, sy))

    print("happy" if possible else "sad")
