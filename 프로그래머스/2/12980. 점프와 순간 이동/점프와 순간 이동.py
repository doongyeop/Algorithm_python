def solution(n):
    ans = 0
    target = n
    while target != 0:
        if target % 2 == 1:
            target -= 1
            ans += 1
        else:
            target /= 2

    return ans

