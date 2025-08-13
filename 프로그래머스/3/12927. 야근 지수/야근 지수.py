import heapq

def solution(n, works):
    
    remains = [-w for w in works]
    heapq.heapify(remains)
    
    for _ in range(n):
        if not remains:
            break
        
        temp = -heapq.heappop(remains)
        if temp <= 0:
            break
        temp -= 1
        heapq.heappush(remains, -temp)
    
    
    return sum((x ** 2) for x in remains)  
