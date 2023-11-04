import sys

n = int(sys.stdin.readline())
operations = []
stack = []

curr = 1
isPossible = True
for _ in range(n):
    number = int(sys.stdin.readline())

    for i in range(curr, number + 1):
        stack.append(i)
        operations.append("+")
        curr = i + 1

    
    if stack and stack[-1] == number:
        stack.pop()
        operations.append("-")
    else:
        isPossible = False
        break

if isPossible:
    for operation in operations:
        print(operation)
else:
    print("NO")