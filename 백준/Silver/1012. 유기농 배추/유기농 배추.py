import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def is_in(y, x):
    return 0 <= y < n and 0 <= x < m

def bfs(s_y, s_x):
    q = deque()
    q.append((s_y, s_x))
    visited[s_y][s_x] = True

    while q:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if is_in(ny, nx) and not visited[ny][nx] and farm[ny][nx] == 1:
                visited[ny][nx] = True
                q.append((ny, nx))

for _ in range(t):
    m, n, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and farm[i][j] == 1:
                cnt += 1
                bfs(i, j)

    print(cnt)
