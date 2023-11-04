import sys
stack = []

n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    else:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)