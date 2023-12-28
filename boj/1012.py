from collections import deque
import sys

case_num = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def make_field(rows, cols):
    field = [[0] * cols for _ in range(rows)]
    return field

def plant_cabbage(K):
    for _ in range(K):
        r, c = map(int, sys.stdin.readline().split())
        field[r][c] = 1

def bfs(r, c):
    queue = deque()
    queue.append((r, c))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if field[nx][ny] == 1:
                queue.append((nx, ny))
                field[nx][ny] = 0

for _ in range(case_num):
    M, N, K = map(int, sys.stdin.readline().split())
    result = 0
    field = make_field(M, N)
    plant_cabbage(K)
    
    for r in range(M):
        for c in range(N):
            if field[r][c] == 1:
                bfs(r, c)
                result += 1
    print(result)