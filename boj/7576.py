from collections import deque

M, N = map(int, input().split())
input_arr = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
result = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if input_arr[nx][ny] == -1: continue

            if input_arr[nx][ny] == 0:
                input_arr[nx][ny] = input_arr[x][y] + 1
                queue.append((nx, ny))

for r in range(N):
    for c in range(M):
        if input_arr[r][c] == 1:
            queue.append((r, c))

bfs()

flag = True
for r in range(N):
    for c in range(M):
        if input_arr[r][c] == 0:
            flag = False
            break
        result = max(input_arr[r][c], result)

if flag:
    print(result - 1)
else:
    print(-1)