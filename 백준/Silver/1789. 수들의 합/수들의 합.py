s = int(input())

left, right = 1, s
answer = 0

while left <= right:
    mid = (left + right) // 2
    temp = mid * (mid + 1) // 2

    if temp <= s:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
