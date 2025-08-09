def solution(s):
    times = 0
    zero = 0

    while s != "1":
        zero += s.count('0')     
        s = s.replace('0', '')   
        length = len(s)         
        s = bin(length)[2:]      
        times += 1

    return [times, zero]
