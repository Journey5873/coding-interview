import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] * M
isused = [False] * (N+1)

def solution(k):
    if k == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        if not isused[i]:
            arr[k] = i
            isused[i] = True
            solution(k+1)
            isused[i] = False

solution(0)