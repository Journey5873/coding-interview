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
    
    for i in range(start, N):
        arr[k] = nums[i]
        solution(k+1, i)
    return

solution(0, 0)