import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

t = int(input())

for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    dist = [INF] * (n + 1)

    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    dist[c] = 0
    q = []
    heapq.heappush(q, (0, c))

    while q:
        time, now = heapq.heappop(q)
        if dist[now] < time: continue

        for next_pc, next_time in graph[now]:
            total_time = time + next_time
            if total_time < dist[next_pc]:
                dist[next_pc] = total_time
                heapq.heappush(q, (total_time, next_pc))
    ans = 0
    MAX = -1
    for d in dist:
        if d != INF:
            ans += 1
            MAX = max(MAX, d)

    print("{} {}".format(ans, MAX))
