from itertools import product as p

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

result = sorted(list(set(p(nums, repeat = m))))

for r in result:
    print(" ".join(map(str, r)))
