import sys
input = sys.stdin.readline

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
max_egg = 0

def solution(k, broken_egg):
    global max_egg

    if k == N:
        max_egg = max(max_egg, broken_egg)
        return
    
    if eggs[k][0] <= 0 or broken_egg == N - 1:
        solution(k+1, broken_egg)
        return
    
    temp = broken_egg
    for i in range(N):
        
        if k == i or eggs[i][0] <= 0:
            continue

        eggs[k][0] -= eggs[i][1]
        eggs[i][0] -= eggs[k][1]

        if eggs[k][0] <= 0:
            broken_egg += 1
        if eggs[i][0] <= 0:
            broken_egg += 1

        solution(k+1, broken_egg)

        eggs[k][0] += eggs[i][1]
        eggs[i][0] += eggs[k][1]

        broken_egg = temp

    return max_egg

solution(0, 0)
print(max_egg)