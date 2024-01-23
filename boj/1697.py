from collections import deque

N, K = map(int, input().split())
visited = [0 for _ in range(100001)]

def bfs(x):
    queue = deque()
    queue.append(x)

    while queue:
       x = queue.popleft()

       if x == K:
           return visited[x]

       for temp in (x-1, x+1, x*2):
           
           if temp < 0 or temp > 100000:
               continue
           if visited[temp] == 0:
               visited[temp] = visited[x] + 1
               queue.append(temp)
               
print(bfs(N))