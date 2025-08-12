from collections import deque

def solution(priorities, location):
    q = deque()
    
    for i in range(0, len(priorities)):
        if i == location:
            q.append([priorities[i], -1])
        else:
            q.append([priorities[i], 0])
    
    answer = 0
    
    while True:
        standard = max(q, key = lambda x: x[0])[0]
        first, target = q.popleft()
        if first == standard:
            answer += 1  
            if target == -1:
                return answer
        else:
            q.append([first, target])
        
            
    
    return answer