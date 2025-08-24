# 계란끼리 충돌 -> 내구도 상대 계란의 무게만큼 깎임
# 내구도 0 이하 -> 깨짐
# 1. 가장 왼쪽의 계란을 든다
# 2. 다른 계란 중 하나를 친다.
# 3. 오른쪽 계란 하나씩

import sys

input = sys.stdin.readline

# class Egg:
#     def __init__(self, durability, weight):
#         self.durability = durability
#         self.weight = weight
#         self.is_broken = False
#
# def hit(egg1, egg2):
#     if egg1.is_broken or egg2.is_broken:
#         return
#
#     egg1.durability -= egg2.weight
#     egg2.durability -= egg1.weight
#
#     if egg1.durability <= 0:
#         egg1.is_broken = True
#     if egg2.durability <= 0:
#         egg2.is_broken = True
# n = int(input())
#
# eggs = [map(int, input().split()) for _ in range(n)]
#

n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
MAX = 0

def hit_egg(idx):
    global MAX

    if idx == n:
        cnt = sum(1 for e in eggs if e[0] <= 0)
        MAX = max(MAX, cnt)
        return

    if eggs[idx][0] <= 0:
        hit_egg(idx + 1)
        return

    hit = False
    for i in range(n):
        if i == idx or eggs[i][0] <= 0:
            continue

        eggs[idx][0] -= eggs[i][1]
        eggs[i][0] -= eggs[idx][1]
        hit = True

        hit_egg(idx + 1)

        eggs[idx][0] += eggs[i][1]
        eggs[i][0] += eggs[idx][1]


    if not hit:
        hit_egg(idx + 1)

hit_egg(0)
print(MAX)