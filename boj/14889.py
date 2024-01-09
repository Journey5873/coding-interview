import sys

N = int(sys.stdin.readline())
board = []
min_value = sys.maxsize

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
visited = [False for _ in range(N)]

def back_tracking(depth, idx):
    global min_value
    if depth == N//2:
        team_A, team_B = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    team_A += board[i][j]
                elif not visited[i] and not visited[j]:
                    team_B += board[i][j]
        min_value = min(min_value, abs(team_A-team_B))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            back_tracking(depth+1, i+1)
            visited[i] = False
back_tracking(0, 0)
print(min_value)