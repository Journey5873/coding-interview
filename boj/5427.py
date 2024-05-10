from collections import deque

T = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def fire_bfs():
    while fire_queue:
        x, y = fire_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if matrix[nx][ny] != "#" and fire_dist[nx][ny] == -1:
                fire_dist[nx][ny] = fire_dist[x][y] + 1
                fire_queue.append((nx, ny))

def s_bfs():
    while s_queue:
        x, y = s_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w: 
                return s_dist[x][y] + 1
            
            if matrix[nx][ny] != "#" and s_dist[nx][ny] == -1 and (s_dist[x][y] + 1 < fire_dist[nx][ny] or fire_dist[nx][ny] == -1):
                s_dist[nx][ny] = s_dist[x][y] + 1
                s_queue.append((nx, ny))
    return "IMPOSSIBLE"

for _ in range(T):

    w, h = map(int, input().split())
    s_queue = deque()
    fire_queue = deque()

    s_dist = [[-1] * w for _ in range(h)]
    fire_dist = [[-1] * w for _ in range(h)]

    matrix = [list(input()) for _ in range(h)]

    for r in range(h):
        for c in range(w):
            if matrix[r][c] == "*":
                fire_dist[r][c] = 0
                fire_queue.append((r, c))
            if matrix[r][c] == "@":
                s_dist[r][c] = 0
                s_queue.append((r, c))

    fire_bfs()
    print(s_bfs())
