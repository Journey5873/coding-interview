from collections import deque

def solution(x, y, n):
    visted = set()
    queue = deque()
    queue.append((x, 0))

    while queue:
        x, cnt = queue.popleft()

        if x > y or x in visted:
            continue

        visted.add(x)

        if x == y:
            return cnt
        
        for temp in (x+n, x*2, x*3):
            if temp <= y and temp not in visted:
                queue.append((temp, cnt+1))

    return -1

print(solution(10, 40, 5))