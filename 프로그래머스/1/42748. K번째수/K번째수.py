def solution(array, commands):
    answer = []
    
    for cmd in commands:
        start = cmd[0] - 1
        end = cmd[1]
        
        target = sorted(array[start:end])
        
        answer.append(target[cmd[2] - 1])
    
    return answer