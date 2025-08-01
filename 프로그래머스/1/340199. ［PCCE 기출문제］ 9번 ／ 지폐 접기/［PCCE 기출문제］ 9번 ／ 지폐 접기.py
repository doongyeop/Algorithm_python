def solution(wallet, bill):
    long = max(wallet)
    short = min(wallet)
    answer = 0
        
    while not can_in(long, short, bill):
        index = 0
        for i in range(2):
            if bill[i] == max(bill):
                index = i
                break;
        bill[i] //= 2
        answer += 1
        
    return answer


def can_in(long, short, bill):
    bill_min = min(bill)
    bill_max = max(bill)
    return bill_max <= long and bill_min <= short