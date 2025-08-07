from collections import deque

m, n, h = map(int, input().split())

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# 토마토 상태 입력
tomatoes = []
for _ in range(h):
    tomato = []
    for j in range(n):
        tomato.append(list(map(int, input().split())))
    tomatoes.append(tomato)

# print(tomatoes)

q = deque()

for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomatoes[z][y][x] == 1:
                q.append((x, y, z))

while q:
    x, y, z = q.popleft()

    for d in range(6):
        nx = x + dx[d]
        ny = y + dy[d]
        nz = z + dz[d]

        if (0 <= nx < m) and (0 <= ny < n) and (0 <= nz < h):
            if tomatoes[nz][ny][nx] == 0:
                tomatoes[nz][ny][nx] = tomatoes[z][y][x] + 1
                q.append((nx, ny, nz))

ans = 0
for floor in tomatoes:
    for r in floor:
        for t in r:
            if t == 0:
                print(-1)
                exit()
            ans = max(ans, t)

print(ans - 1)
