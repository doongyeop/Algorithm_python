def solution(n):
    binary = bin(n)
    ones = binary.count('1')
    number = int(n) + 1
    
    while True:
        number_binary = bin(number)
        
        if number_binary.count('1') == ones:
            return number
        
        number += 1
    
    
    return -1
