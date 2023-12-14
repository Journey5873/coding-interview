from collections import deque

rows, cols = map(int, input().split())
maze = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for r in range(rows):
    maze.append(list(map(int, input().strip())))
dist = [[-1]*cols for _ in range(rows)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    dist[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] 

            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                continue
            if maze[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

bfs(0, 0)
print(dist[rows-1][cols-1]+1)