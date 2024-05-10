N = int(input())

def solution(a, b, n):
    if n == 0:
        return
    
    solution(a, 6-a-b, n-1)
    print(a, b)
    solution(6-a-b, b, n-1)

print(2 ** N - 1)
solution(1, 3, N)