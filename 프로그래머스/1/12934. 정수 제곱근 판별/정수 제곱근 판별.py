import math as m

def solution(n):
    if m.sqrt(n) % 1 == 0:
        return m.pow(m.sqrt(n)+1, 2)
    
    return -1