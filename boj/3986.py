import sys

n = int(sys.stdin.readline())

words = [sys.stdin.readline().strip() for i in range(n)]
count = 0

for i in range(n):
    word = words[i]
    stack = []
    is_good_word = True

    for char in word:
        if not stack or stack[-1] != char:
            stack.append(char)
        elif stack and stack[-1] == char:
            stack.pop()
    
    if not stack:
        count += 1

print(count)