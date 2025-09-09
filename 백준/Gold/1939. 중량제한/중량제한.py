import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

plantA, plantB = map(int, input().split())

def bfs(limit):
    visited = [False] * (N + 1)
    q = deque([plantA])
    visited[plantA] = True

    while q:
        now = q.popleft()
        if now == plantB:
            return True
        for next, weight in graph[now]:
            if not visited[next] and weight >= limit:
                visited[next] = True
                q.append(next)
    return False

l, r = 1, 1_000_000_000
answer = 0

while l <= r:
    m = (l + r) // 2
    if bfs(m):
        answer = m
        l = m + 1
    else:
        r = m - 1

print(answer)
