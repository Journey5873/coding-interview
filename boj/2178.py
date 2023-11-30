from collections import deque
import sys

rows, cols = map(int, input().split())
maze = []

for r in range(rows):
    maze.append(list(map(int, input().rstrip())))
dist = [[-1 for j in range(cols)] for i in range(rows)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(maze, dist, row, col):
    queue = deque()

    queue.append((row, col))
    dist[row][col] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                continue
            if maze[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    
bfs(maze, dist, 0, 0)
print(dist[rows-1][cols-1]+1)