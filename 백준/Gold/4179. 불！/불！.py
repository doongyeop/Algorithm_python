import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
maps = [[""] * c for _ in range(r)]
visited = [[False] * c for _ in range(r)]

jihun = deque()
fire = deque()

for i in range(r):
    line = str(input().strip())
    for j in range(c):
        maps[i][j] = line[j]
        if maps[i][j] == "J":
            jihun.append((i, j))
            visited[i][j] = True
        if maps[i][j] == "F":
            fire.append((i, j))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def is_in(x, y):
    return 0 <= x < r and 0 <= y < c

def bfs():
    time = 0
    while jihun:
        time += 1

        fire_size = len(fire)
        for _ in range(fire_size):
            fx, fy = fire.popleft()
            for d in range(4):
                fnx = fx + dx[d]
                fny = fy + dy[d]
                if not is_in(fnx, fny):
                    continue
                if maps[fnx][fny] == "#" or maps[fnx][fny] == "F":
                    continue
                maps[fnx][fny] = "F"
                fire.append((fnx, fny))

        jihun_size = len(jihun)
        for _ in range(jihun_size):
            x, y = jihun.popleft()
            for d in range(4):
                gnx = x + dx[d]
                gny = y + dy[d]
                if not is_in(gnx, gny):
                    return time
                if maps[gnx][gny] == "." and not visited[gnx][gny]:
                    visited[gnx][gny] = True
                    jihun.append((gnx, gny))

    return -1

result = bfs()
print(result if result != -1 else "IMPOSSIBLE")
