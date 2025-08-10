import math

def solution(arr):

    a = arr[0]
    for i in range(1, len(arr)):
        a = a * arr[i] // math.gcd(a, arr[i])
        
    return a
