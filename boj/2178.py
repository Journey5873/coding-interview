from collections import deque

N, M = map(int, input().split())
input_arr = [list(map(int, input())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    queue = deque()
    dist[0][0] = 1
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue

            if input_arr[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    return dist[N - 1][M - 1]

print(bfs())