from collections import deque

cols, rows = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(rows)]
queue = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                continue

            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))

def calculate_min_days():
    min_day = 0
    for r in range(rows):
        for c in range(cols):
            if box[r][c] == 0:
                return -1
            min_day = max(min_day, box[r][c])
    return min_day - 1

for r in range(rows):
    for c in range(cols):
        if box[r][c] == 1:
            queue.append((r, c))

bfs()
print(calculate_min_days())