from itertools import combinations

def solution(number):
    answer = 0
    for trio in combinations(number, 3):
        if sum(trio) == 0:
            answer += 1
    return answer
