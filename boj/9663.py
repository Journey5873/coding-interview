import sys
input = sys.stdin.readline

N = int(input())
isused_c = [False] * N
isused_up = [False] * (N * 2 - 1)
isused_down = [False] * (N * 2 - 1)
cnt = 0

def solutio(r):
    global cnt
    
    if r == N:
        cnt += 1
        return 
    
    for c in range(N):
        if not isused_c[c] and not isused_up[r+c] and not isused_down[(N-1)+(r-c)]:
            isused_c[c] = True
            isused_up[r+c] = True
            isused_down[(N-1)+(r-c)] = True
            solutio(r+1)
            isused_c[c] = False
            isused_up[r+c] = False
            isused_down[(N-1)+(r-c)] = False
    
solutio(0)
print(cnt)