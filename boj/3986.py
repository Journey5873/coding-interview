N = int(input())

count = 0
for _ in range(N):
    word = input()
    stack = []

    for letter in word:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    
    if not stack:
        count += 1
print(count)