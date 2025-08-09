def solution(s):
    line = s.split(" ")
    for i in range(len(line)):
        if line[i]: 
            line[i] = line[i][0].upper() + line[i][1:].lower()
    answer = " ".join(line)
    return answer
