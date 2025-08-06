from collections import deque

n, m, v = map(int, input().split())

maps = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    f, t = map(int, input().split())
    maps[f][t] = 1
    maps[t][f] = 1

visited = [False] * (n + 1)


def dfs(x):
    visited[x] = True
    print(x, end=' ')
    for i in range(1, n + 1):
        if maps[x][i] == 1 and not visited[i]:
            dfs(i)


def bfs(x):
    queue = deque([x])
    visited[x] = True

    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for i in range(1, n + 1):
            if maps[x][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
