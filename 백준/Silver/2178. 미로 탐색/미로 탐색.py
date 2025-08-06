from collections import deque

n, m = map(int, input().split())

maze = [[0] * m for _ in range(n)]
for i in range(n):
    strs = input()
    maze[i] = list(map(int, strs))

# print(maze)

visited = [[False] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    queue = deque([(x, y, 1)])
    visited[x][y] = True

    while queue:
        cx, cy, dist = queue.popleft()

        if cx == n - 1 and cy == m - 1:
            return dist

        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

    return -1


print(bfs(0, 0))
