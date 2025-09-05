import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)
prev = [0] * (n + 1)

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

apart, goal = map(int, input().split())

def dijkstra(start):
    dist[start] = 0
    q = [(0, start)]
    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for next_city, next_cost in graph[now]:
            total_cost = cost + next_cost
            if total_cost < dist[next_city]:
                dist[next_city] = total_cost
                prev[next_city] = now
                heapq.heappush(q, (total_cost, next_city))

dijkstra(apart)

path = []
cur = goal
while cur != 0:
    path.append(cur)
    cur = prev[cur]
path.reverse()

print(dist[goal])
print(len(path))
print(' '.join(map(str, path)))
