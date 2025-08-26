from collections import deque

def solution(begin, target, words):
    
    def one_diff(before, after):
        if len(before) != len(after):
            return False
        
        cnt = 0
        for i in range(len(before)):
            if before[i] != after[i]:
                cnt += 1
            
        return cnt == 1
    
    def bfs():
        q = deque([(begin, 0)])
        visited = set([begin])

        while q:
            cur, cnt = q.popleft()
            if cur == target:
                return cnt  
            for w in words:
                if w not in visited and one_diff(cur, w):
                    visited.add(w)
                    q.append((w, cnt + 1))
        return 0 

    return bfs()

