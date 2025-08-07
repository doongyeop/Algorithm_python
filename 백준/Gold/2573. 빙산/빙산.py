import sys

sys.setrecursionlimit(100_000)

n, m = map(int, input().split())
icebergs = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

highest = map(max, icebergs)


def melt():
    sea = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if icebergs[i][j] > 0:
                cnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < n and 0 <= ny < m:
                        if icebergs[nx][ny] <= 0:
                            cnt += 1
                sea[i][j] = cnt

    for i in range(n):
        for j in range(m):
            if sea[i][j] > 0:
                icebergs[i][j] = max(0, icebergs[i][j] - sea[i][j])


def dfs(i, j, visited):
    visited[i][j] = True

    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and icebergs[nx][ny] > 0:
                dfs(nx, ny, visited)


year = 0
while True:
    visited = [[False] * m for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            if icebergs[i][j] > 0 and not visited[i][j]:
                dfs(i, j, visited)
                count += 1

    if count == 0:
        print(0)
        break
    if count >= 2:
        print(year)
        break

    melt()
    year += 1
