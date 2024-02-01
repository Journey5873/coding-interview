from collections import deque

N = int(input())
picture = [list(input().strip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cb_visted = [[0] * N for _ in range(N)]
cnt = 0
cb_cnt = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(r, c, color):
    queue = deque()
    queue.append((r, c))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if picture[nx][ny] == color and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

def cb_bfs(r, c, color):
    queue = deque()
    queue.append((r, c))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if color == "B" and picture[nx][ny] == color and cb_visted[nx][ny] == 0:
                cb_visted[nx][ny] = 1
                queue.append((nx, ny))
            elif color != "B" and picture[nx][ny] != "B" and cb_visted[nx][ny] == 0:
                cb_visted[nx][ny] = 1
                queue.append((nx, ny))


for i in range(N):
    for j in range(N):
        
        if visited[i][j] == 0:
            bfs(i, j, picture[i][j])
            cnt += 1

        if cb_visted[i][j] == 0:
            cb_bfs(i, j, picture[i][j])
            cb_cnt += 1

print(cnt)
print(cb_cnt)
