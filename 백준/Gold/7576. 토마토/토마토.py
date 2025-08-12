import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
tomatoes = []
for i in range(n):
    tomatoes.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()

for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            q.append((i, j, 0))


def bfs():
    ans = 0
    while q:
        x, y, date = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = 1
                q.append((nx, ny, date + 1))
                ans = max(ans, date + 1)

    if any(0 in tomato for tomato in tomatoes):
        return -1
    return ans

print(bfs())
