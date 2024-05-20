import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def solution(curr, sum):
    global cnt
    
    if curr == N:
        if sum == S:
            cnt += 1
        return

    solution(curr+1, sum)
    solution(curr+1, sum+arr[curr])
    
solution(0, 0)
if S == 0: cnt -= 1
print(cnt)