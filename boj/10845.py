from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    command = input().split()
    queue_cmd = command[0]

    if queue_cmd == "push":
        queue.append(command[1])
    elif queue_cmd == "pop":
        print(-1) if not queue else print(queue.popleft())
    elif queue_cmd == "size":
        print(len(queue))
    elif queue_cmd == "empty":
        print(1) if not queue else print(0)
    elif queue_cmd == "front":
        print(-1) if not queue else print(queue[0])
    else:
        print(-1) if not queue else print(queue[-1])