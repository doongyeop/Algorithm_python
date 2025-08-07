import sys

input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
MAX = 100_001
row = [0] * MAX


def bfs():
    q = deque()
    q.append(n)

    while q:
        curr = q.popleft()

        if curr == k:
            print(row[curr])
            break

        for next in (curr - 1, curr + 1, curr * 2):
            if 0 <= next < MAX and row[next] == 0:
                row[next] = row[curr] + 1
                q.append(next)


bfs()
