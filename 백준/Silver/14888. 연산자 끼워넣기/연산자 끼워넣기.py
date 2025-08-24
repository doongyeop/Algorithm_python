import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

MIN = 9_876_543_210
MAX = -9_876_543_210


def calculate(idx, cur):
    global MIN, MAX
    if idx == n:
        MIN = min(MIN, cur)
        MAX = max(MAX, cur)
        return

    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1
            if i == 0:
                calculate(idx + 1, cur + nums[idx])
            elif i == 1:
                calculate(idx + 1, cur - nums[idx])
            elif i == 2:
                calculate(idx + 1, cur * nums[idx])
            else:
                if cur < 0:
                    calculate(idx + 1, -(-cur // nums[idx]))
                else:
                    calculate(idx + 1, cur // nums[idx])
            ops[i] += 1


calculate(1, nums[0])
print(MAX)
print(MIN)
