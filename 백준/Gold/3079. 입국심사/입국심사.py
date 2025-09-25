import sys

input = sys.stdin.readline

n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]

left = 0
right = max(times) * m

while left < right:
    mid = (left + right) // 2
    people = 0
    for t in times:
        people += mid // t
        if people >= m:
            break

    if people >= m:
        right = mid
    else:
        left = mid + 1

print(left)
