import sys

input = sys.stdin.readline

n, m = map(int, input().split())
vills = [list(map(int, input().split())) for _ in range(n)]

chickens = []
for i in range(n):
    for j in range(n):
        if vills[i][j] == 2:
            chickens.append([i, j])

MIN = 15_686

chosen = []


def deliver(chickens, idx, chosen):
    global MIN
    if len(chosen) == m:
        min_dist = 0
        for i in range(n):
            for j in range(n):
                if vills[i][j] == 1:
                    temp = 15_686
                    for c in chosen:
                        dist = abs(i - c[0]) + abs(j - c[1])
                        temp = min(temp, dist)
                    min_dist += temp
        MIN = min(MIN, min_dist)
        return

    for i in range(idx, len(chickens)):
        chosen.append(chickens[i])
        deliver(chickens, i + 1, chosen)
        chosen.remove(chickens[i])


deliver(chickens, 0, chosen)

print(MIN)
