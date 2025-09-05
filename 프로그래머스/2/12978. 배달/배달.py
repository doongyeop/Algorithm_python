import heapq

def solution(N, road, K):
    answer = 0
    INF = int(10e9)
    
    graph = [[] for _ in range(N + 1)]
    dist = [INF] * (N + 1)
    
    for ro in road:
        a, b, c = ro
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    q = []
    dist[1] = 0
    heapq.heappush(q, (0, 1))
    while q:
        time, now = heapq.heappop(q)
        
        if dist[now] < time: continue
        
        for next_city, next_time in graph[now]:
            temp = time + next_time
            if temp < dist[next_city]:
                dist[next_city] = temp
                heapq.heappush(q, (temp, next_city))

                
    return sum(1 for d in dist if d <= K)