def solution(a, b, n):
    # 빈병 a개 반납 = 콜라 b개, 빈병 n개
    answer = 0
    while n >= a:
        cokes = (n // a) * b
        answer += cokes
        n = n % a
        n += cokes
    
    return answer