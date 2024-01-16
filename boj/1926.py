from collections import deque
import sys

rows, cols = map(int, input().split())
drawing_paper = []
widest_area = 0
total_cnt = 0

for r in range(rows):
    drawing_paper.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(r, c):
    queue = deque()
    queue.append((r, c))

    drawing_paper[r][c] = 0
    area = 1 

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

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
            area = bfs(r, c)
            widest_area = max(area, widest_area)
            total_cnt += 1

print(total_cnt)    
print(widest_area)

