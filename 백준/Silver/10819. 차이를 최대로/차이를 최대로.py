import sys
from itertools import permutations as perm

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

MAX = 0

all_permutations = perm(nums)

for p in all_permutations:
    temp = 0
    for i in range(n - 1):
        temp += abs(p[i] - p[i + 1])

    if temp > MAX:
        MAX = temp

print(MAX)