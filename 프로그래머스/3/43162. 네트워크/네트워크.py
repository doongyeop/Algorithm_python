from collections import deque

def solution(n, computers):    
    answer = 0
    visited = [False] * n

    def bfs(start):
        q = deque()
        q.append(start)
        visited[start] = True

        while q:
            v = q.popleft()
            for i in range(n):
                if not visited[i] and computers[v][i] == 1:
                    visited[i] = True
                    q.append(i)

    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1 

    return answer
