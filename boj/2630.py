import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = [0] * 2

def solution(r, c, n):

    if n == 1:
        result[matrix[r][c]] += 1
        return

    temp = matrix[r][c]
    is_same = True
    for i in range(n):
        for j in range(n):
            if temp != matrix[r+i][c+j]:
                is_same = False
                break
        if not is_same:
            break
    
    if is_same:
        result[temp] += 1
    else:
        solution(r, c, n//2) #1st area
        solution(r, c+(n//2), n//2) #2nd area
        solution(r+(n//2), c, n//2) #3rd area
        solution(r+(n//2), c+(n//2), n//2) #4th area
    return

solution(0, 0, N)
for r in result:
    print(r)
