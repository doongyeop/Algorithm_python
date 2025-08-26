def solution(tickets):
    tickets.sort()  
    visited = [False] * len(tickets)
    path = ["ICN"]
    result = []

    def dfs(current, depth):
        if depth == len(tickets):
            result.append(path[:])
            return
        
        for i, (start, end) in enumerate(tickets):
            if not visited[i] and start == current:
                visited[i] = True
                path.append(end)
                dfs(end, depth + 1)
                path.pop()
                visited[i] = False

    dfs("ICN", 0)
    return result[0]  
