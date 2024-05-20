import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
arr = [0] * M
nums.sort()

def solution(k, start):
    if k == M:
        print(*arr)
        return
    
    latest = 0
    for i in range(start, N):
        if nums[i] != latest:
            arr[k] = nums[i]
            latest = nums[i]
            solution(k+1, i)

solution(0, 0)
