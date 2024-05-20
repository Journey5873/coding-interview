import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
arr = [0] * M
isused = [False] * N


nums.sort()
def solution(k):
    if k == M:
        print(*arr)
        return
    
    latest = 0
    for i in range(N):
        if not isused[i] and latest != nums[i]:
            isused[i] = True
            arr[k] = nums[i]
            latest = nums[i]
            solution(k+1)
            isused[i] = False
    return

solution(0)