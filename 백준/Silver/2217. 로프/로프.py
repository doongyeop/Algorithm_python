n = int(input())

ropes = []
for i in range(n):
    ropes.append(int(input()))

ropes.sort(reverse=True)
MAX = min(ropes) * n
sum = 0

for i, r in enumerate(ropes):
    MAX = max(MAX, r * (i + 1))

print(MAX)
