import sys

stack = []
n = int(sys.stdin.readline())

for _ in range(n):
    money = int(sys.stdin.readline())
    if money == 0:
        if stack:
            stack.pop()
    else:
        stack.append(money)

total = sum(stack)
print(total)