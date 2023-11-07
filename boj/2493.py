import sys

n = int(sys.stdin.readline())

tops = list(map(int, sys.stdin.readline().split()))
stack = []
results = []

for i in range(n):
    while stack:
        if tops[stack[-1]] <= tops[i]:
            stack.pop()
        else:
            results.append(stack[-1]+1)
            break

    # There are no tops higher than current top, so all the elements are poped 
    if not stack:
        results.append(0)
    stack.append(i)
    
for n in results:
    print(n, end=" ")