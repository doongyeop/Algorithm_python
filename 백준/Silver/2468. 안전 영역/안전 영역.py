import sys
sys.setrecursionlimit(10000)

n = int(input())

areas = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

max_height = max(map(max, areas))

def dfs(x, y, h, visited):
    visited[x][y] = True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and areas[nx][ny] > h:
                dfs(nx, ny, h, visited)

ans = 0

for h in range(0, max_height + 1):
    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if areas[i][j] > h and not visited[i][j]:
                dfs(i, j, h, visited)
                cnt += 1

    ans = max(ans, cnt)

print(ans)
