from collections import deque

T = int(input())

dx = [-1, -2, -1, -2, 1, 2, 1, 2]
dy = [-2, -1, 2, 1, -2, -1, 2, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        if x == target_x and y == target_y:
            return matrix[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= I or ny < 0 or ny >= I: continue

            if matrix[nx][ny] == -1:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))


for _ in range(T):
    I = int(input())
    matrix = [[-1] * I for _ in range(I)]
    queue = deque()

    curr_x, curr_y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    matrix[curr_x][curr_y] = 0
    queue.append((curr_x, curr_y))
    print(bfs())