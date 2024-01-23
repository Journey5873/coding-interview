from collections import deque

R, C = map(int, input().split())
maze = [list(input().strip()) for _ in range(R)]

j_dist = [[-1]*C for _ in range(R)]
f_dist = [[-1]*C for _ in range(R)]

j_queue = deque()
f_queue = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def fire_bfs():

    while f_queue:
        x, y = f_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue

            if maze[nx][ny] != "#" and f_dist[nx][ny] == -1:
                f_dist[nx][ny] = f_dist[x][y] + 1
                f_queue.append((nx, ny))

def j_bfs():

    while j_queue:
        x, y = j_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                return j_dist[x][y] + 1

            if maze[nx][ny] != "#" and j_dist[nx][ny] == -1 and (j_dist[x][y] + 1 < f_dist[nx][ny] or f_dist[nx][ny] == -1):
                j_dist[nx][ny] = j_dist[x][y] + 1
                j_queue.append((nx, ny))

    return "IMPOSSIBLE"

for r in range(R):
    for c in range(C):
        if maze[r][c] == "J":
            j_dist[r][c] = 0
            j_queue.append((r, c))
        elif maze[r][c] == "F":
            f_dist[r][c] = 0 
            f_queue.append((r, c))

fire_bfs()
print(j_bfs())