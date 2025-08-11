from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    list1 = []
    list2 = []

    for i in range(0, len(str1) - 1):
        temp = str1[i] + str1[i + 1]
        if temp.isalpha():
            list1.append(temp)
                        
            
    for i in range(0, len(str2) - 1):
        temp = str2[i] + str2[i + 1]
        if temp.isalpha():
            list2.append(temp)
    
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    
    intersect = sum((counter1 & counter2).values())
    union = sum((counter1 | counter2).values())
    
    return 65536 if union == 0 else int(intersect / union * 65536)