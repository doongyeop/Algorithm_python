def solution(left, right):
    answer = 0
        
    for n in range(left, right + 1):
        if sol(n):
            answer -= n
        else:
            answer += n
    
    return answer

def sol(num):
    return (num ** .5) % 1 == 0