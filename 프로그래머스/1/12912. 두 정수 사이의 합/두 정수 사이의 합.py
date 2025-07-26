def solution(a, b):
    if a > b:
        temp = a
        a = b
        b = temp
    return sum(i for i in range(a, b + 1))