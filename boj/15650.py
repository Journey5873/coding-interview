import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] * M

def solution(k, start):
    if k == M:
        print(*arr)
        return
    
    for i in range(start, N+1):
        arr[k] = i
        solution(k+1, i+1)
    return

solution(0, 1)