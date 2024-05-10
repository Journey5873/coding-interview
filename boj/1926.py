from collections import deque

N, M = map(int, input().split())
input_arr = [list(map(int, input().split())) for _ in range(N)]
max_area = 0
total = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):

    queue = deque()
    input_arr[x][y] = 0
    queue.append((x, y))
    area = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue

            if input_arr[nx][ny] == 1:
                input_arr[nx][ny] = 0
                queue.append((nx, ny))
                area += 1
    return area

for r in range(N):
    for c in range(M):
        if input_arr[r][c] == 1:
            total += 1
            max_area = max(bfs(r, c), max_area)

print(total)
print(max_area)