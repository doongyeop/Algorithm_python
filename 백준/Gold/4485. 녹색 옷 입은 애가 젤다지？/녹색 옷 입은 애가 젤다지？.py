import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

idx = 1
while True:
    n = int(input())
    if n == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]

    q = []
    dist[0][0] = cave[0][0]
    heapq.heappush(q, (dist[0][0], 0, 0))

    while q:
        cost, x, y = heapq.heappop(q)
        if dist[x][y] < cost: continue

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                temp = cost + cave[nx][ny]
                if temp < dist[nx][ny]:
                    dist[nx][ny] = temp
                    heapq.heappush(q, (temp, nx, ny))

    print("Problem {}: {}".format(idx, dist[n - 1][n - 1]))
    idx += 1
