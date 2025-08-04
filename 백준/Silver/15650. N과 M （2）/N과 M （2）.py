from itertools import permutations as p

n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]

result = p(nums, m)

for r in result:
    if all(r[i] < r[i + 1] for i in range(len(r) - 1)):
        print(" ".join(map(str, r)))