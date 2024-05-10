from collections import deque

N = int(input())
input_arr = [list(input()) for _ in range(N)]

visited1 = [[-1] * N for _ in range(N)]
visited2 = [[-1] * N for _ in range(N)]

result1 = result2 = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs1(x, y, color):
    queue = deque()
    visited1[x][y] = 1
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue

            if input_arr[nx][ny] == color and visited1[nx][ny] == -1:
                visited1[nx][ny] = 1
                queue.append((nx, ny))

def bfs2(x, y, color):
    is_RG = True
    if color == "B":
        is_RG = False
    
    queue = deque()
    visited2[x][y] = 1
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue

            if is_RG:
                if (input_arr[nx][ny] == "R" or input_arr[nx][ny] == "G") and visited2[nx][ny] == -1:
                    visited2[nx][ny] = 1
                    queue.append((nx, ny))
            else:
                if input_arr[nx][ny] == color and visited2[nx][ny] == -1:
                    visited2[nx][ny] = 1
                    queue.append((nx, ny))


for r in range(N):
    for c in range(N):
        if visited1[r][c] == -1:
            bfs1(r, c, input_arr[r][c])
            result1 += 1
        if visited2[r][c] == -1:
            bfs2(r, c, input_arr[r][c])
            result2 += 1

print(result1, result2)