K = int(input())
stack = []

for _ in range(K):
    money = int(input())
    if stack and money == 0:
        stack.pop()
    else:
        stack.append(money)

total = sum(stack)
print(total)