import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().strip())) for _ in range(N)]

def solution(r, c, n):

    if n == 1:
        print(matrix[r][c], end="")
        return

    temp = matrix[r][c]
    is_same = True
    
    for i in range(n):
        for j in range(n):
            if temp != matrix[r+i][c+j]:
                is_same = False
        if not is_same:
            break
    
    if is_same:
        print(temp, end="")
    else:
        print("(", end="")    
        solution(r, c, n//2) #1st area
        solution(r, c+(n//2), n//2) #2nd area
        solution(r+(n//2), c, n//2) #3rd area
        solution(r+(n//2), c+(n//2), n//2) #4th area
        print(")", end="")

solution(0, 0, N)