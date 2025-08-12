import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
cnt = 0

for c in coins:
    cnt += k // c
    k %= c
    if k == 0: break

print(cnt)
