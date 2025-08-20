def solution(A, B):
    
    arr_a = sorted(A)
    arr_b = sorted(B)

    n = len(A)
    i, j = 0, 0
    answer = 0
    
    while (i < n and j < n):
        if arr_b[j] > arr_a[i]:
            answer += 1
            i += 1
            j += 1
        else:
            j += 1
            
    
    return answer