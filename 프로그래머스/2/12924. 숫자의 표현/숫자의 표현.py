def solution(n):
    start = 1
    end = 1
    current_sum = 1
    answer = 0

    while start <= n and end <= n:
        if current_sum == n:
            answer += 1
            current_sum -= start
            start += 1
        elif current_sum < n:
            end += 1
            current_sum += end
        else:  
            current_sum -= start
            start += 1

    return answer
