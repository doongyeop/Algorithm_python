def solution(today, terms, privacies):
    answer = []
    
    y, m, d = map(int, today.split("."))
    today_int = y * 12 * 28 + m * 28 + d
    
    term = {}
    for t in terms:
        alp, month = t.split()
        term[alp] = int(month)
        
    for i in range(len(privacies)):
        date, alp = privacies[i].split(" ")
        y, m, d = map(int, date.split("."))
        
        target_int = y * 12 * 28 + m * 28 + d + term[alp] * 28 - 1
        if today_int > target_int:
            answer.append(i + 1)
    
    return answer