from collections import deque

N, M, K = map(int, input().split())

matrix = [[0] * M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

max_area = 0

for _ in range(K):
    r, c = map(int, input().split())
    matrix[r - 1][c - 1] = 1

def bfs (r, c):
    queue = deque()
    queue.append((r, c))
    area = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                queue.append((nx, ny))
                area += 1
    
    if area == 0:
        return 0
    return area

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            max_area = max(max_area, bfs(i, j))

print(max_area)