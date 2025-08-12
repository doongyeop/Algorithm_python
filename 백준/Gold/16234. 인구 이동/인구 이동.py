import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def is_in(x, y):
    return 0 <= x < N and 0 <= y < N

def is_open(a, b):
    return L <= abs(a - b) <= R

def bfs(x, y, visited):
    q = deque([(x, y)])
    visited[x][y] = True
    union = [(x, y)]
    total = world[x][y]

    while q:
        cx, cy = q.popleft()

        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if not is_in(nx, ny): continue
            if visited[nx][ny]: continue
            if is_open(world[cx][cy], world[nx][ny]):
                visited[nx][ny] = True
                q.append((nx, ny))
                union.append((nx, ny))
                total += world[nx][ny]

    avg = total // len(union)
    for ux, uy in union:
        world[ux][uy] = avg

    return len(union) > 1

days = 0
while True:
    visited = [[False] * N for _ in range(N)]
    moved = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    moved = True
    if not moved:
        break
    days += 1

print(days)
