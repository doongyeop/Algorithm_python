import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
size = 100_001

N, K = map(int, input().split())

dist = [INF] * (size)
dist[N] = 0

q = []
heapq.heappush(q, (0, N))

while q:
    time, now = heapq.heappop(q)

    if dist[now] < time: continue

    next = now * 2

    if 0 <= next < size and dist[next] > time:
        dist[next] = time
        heapq.heappush(q, (time, next))

    for next in [now - 1, now + 1]:
        if 0 <= next < size and dist[next] > time + 1:
            dist[next] = time + 1
            heapq.heappush(q, (time + 1, next))

print(dist[K])
