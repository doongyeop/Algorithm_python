import sys

input = sys.stdin.readline
from collections import deque

f, s, g, u, d = map(int, input().split())

MAX = f + 1
floors = [0] * MAX


def bfs():
    q = deque([s])
    floors[s] = 1

    while q:
        curr = q.popleft()
        # print(floors)

        if curr == g:
            return floors[curr] - 1

        for next in (curr + u, curr - d):
            if 1 <= next < MAX:
                if floors[next] == 0:
                    floors[next] = floors[curr] + 1
                    q.append(next)

    return "use the stairs"


print(bfs())
