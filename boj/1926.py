from collections import deque
import sys

rows, cols = map(int, sys.stdin.readline().split())
drawing_paper = []
total_drawing = 0
max_area = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for r in range(rows):
    drawing_paper.append(list(map(int, sys.stdin.readline().split())))

def bfs(drawing_paper, row, col):
    queue = deque()

    queue.append((row, col))
    drawing_paper[row][col] = 0
    area = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                continue
            if drawing_paper[nx][ny] == 1:
                drawing_paper[nx][ny] = 0
                queue.append((nx, ny))
                area += 1
    return area

for r in range(rows):
    for c in range(cols):
        if drawing_paper[r][c] == 1:
            area = bfs(drawing_paper, r, c)
            max_area = max(max_area, area)
            total_drawing += 1

print(total_drawing)
print(max_area)
