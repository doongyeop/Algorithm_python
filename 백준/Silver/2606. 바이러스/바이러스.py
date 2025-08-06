from collections import deque

n = int(input())
c = int(input())

network = [[] for _ in range(n + 1)]

for _ in range(c):
    f, t = map(int, input().split())
    network[f].append(t)
    network[t].append(f)

# print(network)

visited = [False] * (n + 1)

def bfs(x):
    q = deque([x])
    visited[x] = True
    cnt = 0

    while q:
        v = q.popleft()
        for w in network[v]:
            if not visited[w]:
                visited[w] = True
                q.append(w)
                cnt += 1

    return cnt

print(bfs(1))
