from collections import deque

N, K = map(int, input().split())
queue = deque()
dist = [-1] * 100001

def bfs(x):
    dist[x] = 0
    queue.append(x)
    while queue:
        x = queue.popleft()

        if x == K:
            return dist[x]
        
        for i in (x - 1, x + 1, x * 2):

            if i < 0 or i > 100000: continue

            if dist[i] == -1:
                dist[i] = dist[x] + 1
                queue.append(i)

print(bfs(N))