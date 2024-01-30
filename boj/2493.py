N = int(input())
tops = list(map(int, input().split()))
stack = []
results = []

for i in range(len(tops)):

    while stack:
        if tops[stack[-1]] < tops[i]:
            stack.pop()
        else:
            results.append(stack[-1] + 1)
            break

    if not stack:
        results.append(0)
    stack.append(i)

print(*results)