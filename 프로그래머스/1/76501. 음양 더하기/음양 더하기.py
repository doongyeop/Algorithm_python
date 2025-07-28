def solution(absolutes, signs):
    answer = 0
    
    for s in range(len(signs)):
        if signs[s]:
            answer += absolutes[s]
        else:
            answer -= absolutes[s]
    
    return answer