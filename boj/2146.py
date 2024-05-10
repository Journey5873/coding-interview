# 1. 섬을 순회하여 각 섬마다 다른 번호 부여하기
# 2. labeling 하면서 해당 섬의 가장자리를 구하기
# 3. 섬의 가장자리를 다시 순회하면서 다른 섬까지의 거리를 구하기
# 4. 3번을 진행하면서 현재 min 숫자보다 커질 경우 순회를 중단

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

def label_island_bfs(x, y, island_id):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    queue = deque()
    matrix[x][y] = island_id
    queue.append((x, y))
    edges_queue = deque()

    while queue:
        x, y = queue.popleft()
        is_edge = False
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                # 아직 label이 안 된 경우
                if matrix[nx][ny] == 1:
                    matrix[nx][ny] = island_id
                    queue.append((nx, ny))
                # 현재 좌표가 (x,y) 섬의 가장자리일 경우
                elif matrix[nx][ny] == 0:
                    is_edge = True
        if is_edge:
            edges_queue.append((x, y))
    return edges_queue

def find_min_brige_bfs(isl_id, edges):
    queue = deque(edges)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[-1] * N for _ in range(N)]

    for x, y in edges:
        visited[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 바다이고 아직 방문하지 않았을 경우
                if matrix[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                # 육지이고, 출발한 육지와 다른 육지일 경우
                elif matrix[nx][ny] > 0 and matrix[nx][ny] != isl_id:
                    return visited[x][y]
    return float("inf")

def solution():
    island_id = 2
    edges_dic = {}
    min_dist = float("inf")
    
    # 섬의 번호를 labeling & 가장자리에 인접한 바다 찾기
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 1:
                ret_edges = label_island_bfs(r, c, island_id)
                edges_dic[island_id] = ret_edges
                island_id += 1
    
    # 섬에 인접한 바다에서 다른 섬으로 가는 최단 경로 찾기
    for isl_id, edges in edges_dic.items():
        dist = find_min_brige_bfs(isl_id, edges)
        min_dist = min(dist, min_dist)
    return min_dist

print(solution())