def solution(price, money, count):
    answer = sum(i for i in range(1, count + 1)) * price - money
    
    return 0 if answer < 0 else answer