import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = [0] * 3

def solution(r, c, n):

    if n == 1:
        result[matrix[r][c] + 1] += 1
        return 

    temp = matrix[r][c]
    is_same = True
    for i in range(n):
        for j in range(n):
            if matrix[r+i][c+j] != temp:
                is_same = False
                break
        if not is_same:
            break

    if is_same:
        result[temp + 1] += 1
    else:
        solution(r, c, n//3) #1st area
        solution(r, c+(n//3), n//3) #2nd area
        solution(r, c+((n//3)*2), n//3) #3rd area
        solution(r+(n//3), c, n//3) # 4th area
        solution(r+(n//3), c+(n//3), n//3) # 5th area
        solution(r+(n//3), c+((n//3)*2), n//3) #6th area
        solution(r+((n//3)*2), c, n//3) #7th area
        solution(r+((n//3)*2), c+(n//3), n//3)# 8th area
        solution(r+((n//3)*2), c+((n//3)*2), n//3)#9th area
    return

solution(0, 0, N)

for i in range(3):
    print(result[i])