import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] * M

def solution(k):
    if k == M:
        print(*arr)
        return
    
    for i in range(1, N+1):
        arr[k] = i
        solution(k+1)
    return

solution(0)
