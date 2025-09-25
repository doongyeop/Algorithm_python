import sys

input = sys.stdin.readline

n = int(input())
arr1 = set(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

answer = []
for a in arr2:
    if a in arr1:
        answer.append("1")
    else:
        answer.append("0")

print(" ".join(answer))
