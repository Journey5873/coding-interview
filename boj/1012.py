from collections import deque
import sys

input = sys.stdin.readline
field = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())

def plant_cabbage(k):

    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1

def bfs():

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if 0 <= nx < M and 0 <= ny < N and field[nx][ny] == 1:
                field[nx][ny] = 0
                queue.append((nx, ny))


for _ in range(T):

    M, N, K = map(int, input().split())
    queue = deque()
    count = 0

    field = [[0] * N for _ in range(M)]
    plant_cabbage(K)

    for i in range(M):
        for j in range(N):
            if field[i][j] == 1:
                field[i][j] = 0
                queue.append((i, j))
                bfs()
                count += 1
    print(count)