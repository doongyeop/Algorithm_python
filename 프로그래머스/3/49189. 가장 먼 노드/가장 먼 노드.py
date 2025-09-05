from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a) 

    dist = [-1] * (n + 1)  
    q = deque([1])
    dist[1] = 0

    while q:
        cur = q.popleft()
        for nx in graph[cur]:
            if dist[nx] == -1:
                dist[nx] = dist[cur] + 1
                q.append(nx)

    maxd = max(dist[1:])
    return dist.count(maxd)
