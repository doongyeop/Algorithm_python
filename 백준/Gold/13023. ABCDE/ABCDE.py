import sys
sys.setrecursionlimit(10**3)
input = sys.stdin.readline

n, m = map(int, input().split())
friends = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

visited = [False] * n
found = False

def dfs(idx, depth):
    global found
    if found:
        return
    if depth == 4:
        found = True
        return
    visited[idx] = True
    for next in friends[idx]:
        if not visited[next]:
            dfs(next, depth + 1)
    visited[idx] = False

for i in range(n):
    dfs(i, 0)
    if found:
        break

print(1 if found else 0)
