import heapq
import sys

input = sys.stdin.readline

N = int(input())

former = []
latter = []

for _ in range(N):
    num = int(input())
    if len(former) == len(latter):

        heapq.heappush(former, -num)
    else:
        heapq.heappush(latter, num)

    if latter and -former[0] > latter[0]:
        a = -heapq.heappop(former)
        b = heapq.heappop(latter)
        heapq.heappush(former, -b)
        heapq.heappush(latter, a)

    print(-former[0])
