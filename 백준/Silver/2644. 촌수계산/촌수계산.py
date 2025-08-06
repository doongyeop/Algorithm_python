from collections import deque

n = int(input())
visited = [False] * (n+1)

tar1, tar2 = map(int, input().split())
m = int(input())

peoples = [[] for _ in range(n + 1)]

for i in range(m):
    f, t = map(int, input().split())
    peoples[f].append(t)
    peoples[t].append(f)


# print(peoples)

def bfs(x):
    q = deque([(x, 0)])
    visited[x] = True

    while q:
        v, far = q.popleft()
        for p in peoples[v]:
            if not visited[p]:
                if p == tar2:
                    return far + 1

                visited[p] = True
                q.append((p, far + 1))

    return -1


print(bfs(tar1))
