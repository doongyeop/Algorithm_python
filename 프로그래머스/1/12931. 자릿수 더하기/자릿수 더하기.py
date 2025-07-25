def solution(n):
    answer = 0

    str_list = list(str(n))
    for s in str_list:
        answer += int(s)

    return answer