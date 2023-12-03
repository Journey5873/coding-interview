from collections import deque
import sys

cols, rows = map(int, sys.stdin.readline().split())
box = []

for r in range(rows):
    box.append(list(map(int, sys.stdin.readline().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque()
for r in range(rows):
    for c in range(cols):
        if box[r][c] == 1:
            queue.append((r, c))

def bfs(box, queue, rows, cols):

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
        
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                continue
            if box[nx][ny] == 0:
                queue.append((nx, ny))
                box[nx][ny] = box[x][y] + 1
                

bfs(box, queue, rows, cols)

count = 0
for r in range(rows):
    for c in range(cols):
        if box[r][c] == 0:
            print(-1)
            exit()
        count = max(count, box[r][c])
print(count - 1)