import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

if all(all(cell == 0 for cell in row) for row in paper):
    print(0)
    print(0)
    exit(0)

visited = [[False] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

pictures = []

def bfs(i, j):
    q = deque()
    visited[i][j] = True
    q.append((i, j))
    size = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and paper[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
                size += 1
    pictures.append(size)

for i in range(n):
    for j in range(m):
        if not visited[i][j] and paper[i][j] == 1:
            bfs(i, j)

print(len(pictures))
print(max(pictures))
