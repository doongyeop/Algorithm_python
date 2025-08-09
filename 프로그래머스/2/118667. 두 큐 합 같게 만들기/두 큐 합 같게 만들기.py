from collections import deque

def solution(queue1, queue2):
    total_sum = sum(queue1) + sum(queue2)
    if total_sum % 2 != 0:
        return -1  # 전체 합이 홀수면 불가능
    
    target = total_sum // 2
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    max_ops = len(queue1) * 3  
    count = 0
    
    while count <= max_ops:
        if sum1 == target:
            return count
        
        if sum1 > target:
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
        else:
            num = q2.popleft()
            q1.append(num)
            sum2 -= num
            sum1 += num
        
        count += 1
    
    return -1
