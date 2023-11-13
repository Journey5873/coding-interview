from collections import deque
import sys

queue = deque()

def push(x):
    queue.append(int(x))

def pop():
    return queue.popleft() if queue else -1

def size():
    return len(queue)

def empty():
    return 1 if not queue else 0

def front():
    return queue[0] if queue else -1

def back():
    return queue[-1] if queue else -1

commands = {
    "push": push,
    "pop": pop,
    "front": front,
    "back": back,
    "size": size,
    "empty": empty,
}

n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()
    cmd = command[0]

    if cmd == "push":
        commands[cmd](command[1])
    else:
        result = commands[cmd]()
        print(result)