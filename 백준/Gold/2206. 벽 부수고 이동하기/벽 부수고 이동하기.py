import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]


def is_in(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y):
    q = deque()
    q.append((x, y, 1, 0))
    visited[x][y][0] = True

    while q:
        x, y, dist, wall = q.popleft()

        if x == n - 1 and y == m - 1:
            return dist

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not is_in(nx, ny):
                continue

            if maps[nx][ny] == 0 and not visited[nx][ny][wall]:
                visited[nx][ny][wall] = True
                q.append((nx, ny, dist + 1, wall))

            if maps[nx][ny] == 1 and wall == 0 and not visited[nx][ny][1]:
                visited[nx][ny][1] = True
                q.append((nx, ny, dist + 1, 1))

    return -1


print(bfs(0, 0))
