def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        arr = arr1[i] | arr2[i]

        binary = format(arr, f'0{n}b')

        line = ''.join('#' if b == '1' else ' ' for b in binary)
        answer.append(line)

    return answer
