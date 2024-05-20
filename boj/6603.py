import sys
input = sys.stdin.readline

def solution(k, start):
    if k == 6:
        print(*arr)
        return
    
    for i in range(start, len(S)):
        arr[k] = S[i]
        solution(k+1, i+1)
    
    return

while True:
    input_arr = list(map(int, input().split()))
    K = input_arr[0]
    S = input_arr[1:]
    arr = [0] * 6

    if K == 0:
        exit()

    solution(0, 0)
    print()