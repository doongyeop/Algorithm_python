from itertools import permutations as p

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

result = p(nums, m)

for r in result:
    print(" ".join(map(str, r)))
