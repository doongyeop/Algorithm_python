def solution(numbers):
    numbers_str = list(map(str, numbers))
    
    sorted_numbers = sorted(numbers_str, key=lambda x: x*3, reverse=True)
    answer = ''.join(sorted_numbers)

    if answer[0] == '0':
        return '0'
    
    return answer