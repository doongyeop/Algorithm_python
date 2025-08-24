import sys

input = sys.stdin.readline

n, s = map(int, input().split())

arr = list(map(int, input().split()))


cnt = 0
def sum_of_segments(idx, sum):
    global cnt
    if idx == n:
        if sum == s:
            cnt += 1
        return

    sum_of_segments(idx + 1, sum + arr[idx])
    sum_of_segments(idx + 1, sum)

sum_of_segments(0, 0)
if s == 0:
    cnt -= 1

print(cnt)