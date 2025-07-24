def solution(numbers):
    numbers.sort()
    return numbers.pop() * numbers.pop()