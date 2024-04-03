def backtracking(idx, broken_egg):
    global max_egg

    if idx == N:
        max_egg = max(max_egg, broken_egg)
        return
    
    if egg[idx][0] <= 0 or broken_egg == N - 1:
        backtracking(idx + 1, broken_egg)
        return

    copied_egg = broken_egg
    for i in range(N):
        if i == idx or egg[i][0] <= 0:
            continue

        egg[idx][0] -= egg[i][1]
        egg[i][0] -= egg[idx][1]

        if egg[i][0] <= 0:
            broken_egg += 1
        if egg[idx][0] <= 0:
            broken_egg += 1

        backtracking(idx + 1, broken_egg)
        
        egg[idx][0] += egg[i][1]
        egg[i][0] += egg[idx][1]
        broken_egg = copied_egg
        
    return max_egg

N = int(input())
egg = [list(map(int, input().split())) for _ in range(N)]
max_egg = 0
backtracking(0, 0)
print(max_egg)