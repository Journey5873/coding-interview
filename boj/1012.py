from collections import deque

T = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):

    queue = deque()
    input_arr[x][y] = 0
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N: continue

            if input_arr[nx][ny] == 1:
                input_arr[nx][ny] = 0
                queue.append((nx, ny))


for _ in range(T):
    M, N, K = map(int, input().split())
    input_arr = [[0] * N for _ in range(M)]
    total = 0

    for _ in range(K):
        r, c = map(int, input().split())
        input_arr[r][c] = 1

    for r in range(M):
        for c in range(N):
            if input_arr[r][c] == 1:
                total += 1
                bfs(r, c)

    print(total)