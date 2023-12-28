from collections import deque
import sys

def fire_bfs():
    while fire_queue:
        x, y = fire_queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                continue

            if maze[nx][ny] != "#" and f_dist[nx][ny] == -1:
                fire_queue.append((nx, ny))
                f_dist[nx][ny] = f_dist[x][y] + 1

def j_bfs():
    while j_queue:
        x, y = j_queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                return j_dist[x][y] + 1

            if maze[nx][ny] == "." and j_dist[nx][ny] == -1 and (f_dist[nx][ny] == -1 or j_dist[x][y] + 1 < f_dist[nx][ny]):
                j_queue.append((nx, ny))
                j_dist[nx][ny] = j_dist[x][y] + 1

    return "IMPOSSIBLE"

rows, cols = map(int, input().split())
maze = []
fire_queue = deque()
j_queue = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for r in range(rows):
    maze.append(list(sys.stdin.readline().strip()))
j_dist = [[-1]*cols for _ in range(rows)]
f_dist = [[-1]*cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        if maze[i][j] == "F":
            fire_queue.append((i, j))
            f_dist[i][j] = 0
        if maze[i][j] == "J":
            j_queue.append((i, j))
            j_dist[i][j] = 0

fire_bfs()
print(j_bfs())


