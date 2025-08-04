from itertools import product as p

n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]

result = p(nums, repeat = m)

for r in result:
        print(" ".join(map(str, r)))