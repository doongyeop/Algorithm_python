def solution(num_list):
    odds = 0

    for n in num_list:
        if n % 2 == 1:
            odds += 1 

    evens = len(num_list) - odds 
    return [evens, odds]
