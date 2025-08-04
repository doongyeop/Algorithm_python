from itertools import combinations_with_replacement as c

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

result = sorted(list(set(c(nums, m))))

for r in result:
    print(" ".join(map(str, r)))
