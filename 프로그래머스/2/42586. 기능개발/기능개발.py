import math

def solution(progresses, speeds):
    remains = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    answer = []
    cur = remains[0]  
    count = 0
    
    for remain in remains:
        if remain <= cur:
            count += 1
        else:
            answer.append(count)
            count = 1
            cur = remain
    answer.append(count)  
    
    return answer
