import heapq

def solution(scoville, K):
    q = []
    for s in scoville:
        heapq.heappush(q, s)
    
    answer = 0
    while q and q[0] < K:
        if len(q) < 2:
            return -1
        first = heapq.heappop(q)
        second = heapq.heappop(q)
        heapq.heappush(q, first + second * 2)
        answer += 1

    return answer
