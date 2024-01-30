from collections import deque

rows, cols = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(rows)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
queue = deque()
day = 0
check = False

def bfs(a,b):
    queue.append((a,b))
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols:
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                elif graph[nx][ny] == 0:
                    count[x][y] += 1
    return 1

while True:
    visited = [[False]*cols for _ in range(rows)]
    count = [[0]*cols for _ in range(rows)]
    result = []
    for i in range(rows):
        for j in range(cols):
            if graph[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i,j))

    for i in range(rows):
        for j in range(cols):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    
    if len(result) == 0: 
        break
    if len(result) >= 2: 
        check = True
        break
    day += 1

if check:        
    print(day)
else:
    print(0)