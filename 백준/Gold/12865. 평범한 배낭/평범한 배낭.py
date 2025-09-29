import sys

input = sys.stdin.readline

n, k = map(int, input().split())

class Knapsack:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

bags = []

for _ in range(n):
    w, v = map(int, input().split())
    bags.append(Knapsack(w, v))

dp = [0] * (k + 1)

for bag in bags:
    for i in range(k, bag.weight - 1, -1):
        dp[i] = max(dp[i], dp[i - bag.weight] + bag.value)

print(dp[k])
