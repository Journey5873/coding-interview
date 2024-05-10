from collections import deque

C, R, H = map(int, input().split())

input_arr = [[list(map(int, input().split())) for _ in range(R)] for _ in range(H)]
visited = [[[-1] * C for _ in range(R)] for _ in range(H)]

queue = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, 0, -1, 0]
dz = [0, 0, 0, 1, 0, -1]

def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= H or ny < 0 or ny >= R or nz < 0 or nz >= C: continue

            if input_arr[nx][ny][nz] == 0 and visited[nx][ny][nz] == -1:
                input_arr[nx][ny][nz] = input_arr[x][y][z] + 1
                visited[nx][ny][nz] = 1
                queue.append((nx, ny, nz))

def get_least_day():
    least_day = 0
    for h in range(H):
        for r in range(R):
            for c in range(C):
                if input_arr[h][r][c] == 0:
                    return -1
                least_day = max(input_arr[h][r][c], least_day)
    return least_day - 1

for h in range(H):
    for r in range(R):
        for c in range(C):
            if input_arr[h][r][c] == 1:
                visited[h][r][c] = 1
                queue.append((h, r, c))

bfs()
print(get_least_day())