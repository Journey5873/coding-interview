from collections import deque

N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]

def bfs():
    visited = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()

    visited[0][0][0] = 1
    queue.append((0, 0, 0))
    
    while queue:
        x, y, is_crashed = queue.popleft()

        # Check if we've reached the bottom-right corner
        if x == N - 1 and y == M - 1:
            return visited[x][y][is_crashed]

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
           
            if 0 <= nx < N and 0 <= ny < M:
                # If the next cell is not a wall and has not been visited yet
                if matrix[nx][ny] == 0 and visited[nx][ny][is_crashed] == -1:
                    visited[nx][ny][is_crashed] = visited[x][y][is_crashed] + 1
                    queue.append((nx, ny, is_crashed))
                # If the next cell is a wall and it has not been visited yet
                elif matrix[nx][ny] == 1 and visited[nx][ny][1] == -1:
                    # If a wall hasn't been broken yet
                    if is_crashed == 0:
                        visited[nx][ny][1] = visited[x][y][is_crashed] + 1
                        queue.append((nx, ny, 1))
                    # If a wall has already been broken
                    elif is_crashed == 1:
                        continue
    return -1
        
def solution():
    result = bfs()
    return result

print(solution())