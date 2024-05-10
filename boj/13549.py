from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def solution(n):
    queue = deque()
    dist = [-1] * 100001
    dx = [2, -1, 1]

    dist[n] = 0
    queue.append(n)
    
    while queue:
        x = queue.popleft()
        
        if x == K:
            return dist[x]
        
        for i in range(3):
            if dx[i] == 2:
                nx = x * 2
                if 0 <= nx < 100001 and dist[nx] == -1:
                    dist[nx] = dist[x]
                    queue.appendleft(nx)
            else:
                nx = x + dx[i]
                if 0 <= nx < 100001 and dist[nx] == -1:
                    dist[nx] = dist[x] + 1
                    queue.append(nx)

print(solution(N))