import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
arr = [0] * M
isused = [False] * N
nums.sort()

def solution(k, start):
    if k == M:
        print(*arr)
        return
    
    for i in range(start, N):
        if not isused[i]:
            isused[i] = True
            arr[k] = nums[i]
            solution(k+1, i+1)
            isused[i] = False
    return

solution(0, 0)