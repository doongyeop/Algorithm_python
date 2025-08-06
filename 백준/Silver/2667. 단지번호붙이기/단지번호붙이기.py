n = int(input())

maps = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for i in range(n):
    maps[i] = list(map(int, input()))
# print(maps)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

ans = []


def dfs(i, j):
    cnt = 1
    visited[i][j] = True

    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]

        if not (0 <= nx < n and 0 <= ny < n): continue
        if visited[nx][ny] or maps[nx][ny] == 0: continue

        cnt += dfs(nx, ny)

    return cnt


for i in range(n):
    for j in range(n):
        if maps[i][j] != 0 and not visited[i][j]:
            ans.append(dfs(i, j))

ans.sort()
print(len(ans))
for a in ans:
    print(a)
