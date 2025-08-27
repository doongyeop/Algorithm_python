def solution(dirs):
    moves = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    
    x, y = 0, 0
    visited = set()  
    answer = 0

    for d in dirs:
        dx, dy = moves[d]
        nx, ny = x + dx, y + dy
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path = ((x, y), (nx, ny))
            reverse = ((nx, ny), (x, y))
            if path not in visited:
                visited.add(path)
                visited.add(reverse) 
                answer += 1
            x, y = nx, ny

    return answer
