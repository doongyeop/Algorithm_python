def solution(x):
    n = x
    sum_each = 0
    while n > 0:
        sum_each += (n % 10)
        n //= 10
    
    return x % sum_each == 0