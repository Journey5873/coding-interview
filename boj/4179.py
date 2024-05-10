from collections import deque

N, M = map(int, input().split())
input_arr = [list(input()) for _ in range(N)]

j_queue = deque()
fire_queue = deque()
j_dist = [[-1] * M for _ in range(N)]
fire_dist = [[-1] * M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def fire_bfs():
    while fire_queue:
        x, y = fire_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue

            if input_arr[nx][ny] != "#" and fire_dist[nx][ny] == -1:
                fire_dist[nx][ny] = fire_dist[x][y] + 1
                fire_queue.append((nx, ny))

def j_bfs():
    while j_queue:
        x, y = j_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M: 
                return j_dist[x][y] + 1
            
            if input_arr[nx][ny] != "#" and j_dist[nx][ny] == -1 and (j_dist[x][y] + 1 < fire_dist[nx][ny] or fire_dist[nx][ny] == -1):
                j_dist[nx][ny] = j_dist[x][y] + 1
                j_queue.append((nx, ny))
    return "IMPOSSIBLE"            

for r in range(N):
    for c in range(M):
        if input_arr[r][c] == "F":
            fire_dist[r][c] = 0
            fire_queue.append((r, c))
        if input_arr[r][c] == "J":
            j_dist[r][c] = 0
            j_queue.append((r, c))

fire_bfs()
print(j_bfs())