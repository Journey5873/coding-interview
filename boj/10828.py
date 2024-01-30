import sys
input = sys.stdin.readline 
test_case = int(input())
stack = []

for _ in range(test_case):
    command = input().split()
    stack_cmd = command[0]

    if stack_cmd == "push":
        stack.append(int(command[1]))
    elif stack_cmd == "pop":
        print(-1) if not stack else print(stack.pop())
    elif stack_cmd == "size":
        print(len(stack))
    elif stack_cmd == "empty":
        print(1) if not stack else print(0)
    else:
        print("-1") if not stack else print(stack[-1])