import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
arr = [0] * M
isused = [False] * (N+1)
nums.sort()

def solution(k):
    if k == M:
        print(*arr)
        return
    
    for i in range(N):
        if not isused[i]:
            arr[k] = nums[i]
            isused[i] = True
            solution(k+1)
            isused[i] = False
    return

solution(0)