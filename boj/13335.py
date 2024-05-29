from collections import deque
import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))
arr = [0] * w

def solution():
    result = 0

    while trucks:

        arr.pop(0)

        if sum(arr) + trucks[0] <= L:
            arr.append(trucks.popleft())
        else:
            arr.append(0)
        
        result += 1
    return result + len(arr)

print(solution())