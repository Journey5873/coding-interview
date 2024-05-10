from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def bfs(x, y, visited, sea_cnt):

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    queue = deque()
    visited[x][y] = 1
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] > 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                elif matrix[nx][ny] == 0:
                    sea_cnt[x][y] += 1
    return 1


def solution():
    day = 0
    while True:
        visited = [[-1] * M for _ in range(N)]
        sea_cnt = [[0] * M for _ in range(N)]
        ret = 0

        for r in range(N):
            for c in range(M):
                if matrix[r][c] > 0 and visited[r][c] == -1:
                    ret += bfs(r, c, visited, sea_cnt)
        
        if ret >= 2:
            return day
        elif ret == 0:
            return 0
        
        for r in range(N):
            for c in range(M):
                matrix[r][c] -= sea_cnt[r][c]
                if matrix[r][c] < 0:
                    matrix[r][c] = 0
        
        day += 1


print(solution())