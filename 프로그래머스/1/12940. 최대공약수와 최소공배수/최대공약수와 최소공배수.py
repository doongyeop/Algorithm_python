import math as h

def solution(n, m):
    gcd = h.gcd(n, m)
    lcm = n * m // gcd
    return [gcd, lcm]
