import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

m, n = map(int, input().split())
dist = [[INF] * m for _ in range(n)]
grid = [[int(l) for l in input().strip()] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dijkstra(i, j):
    dist[i][j] = 0
    q = [(0, i, j)]
    while q:
        cost, x, y = heapq.heappop(q)
        if dist[x][y] < cost: continue

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                temp = cost + grid[nx][ny]
                if temp < dist[nx][ny]:
                    dist[nx][ny] = temp
                    heapq.heappush(q, (temp, nx, ny))


dijkstra(0, 0)
print(dist[n - 1][m - 1])
