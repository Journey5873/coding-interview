import sys

while True:
    sentence = input()
    stack = []
    is_balanced = True

    if sentence == ".":
        break

    for char in sentence:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                is_balanced = False
                break
        elif char == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                is_balanced = False
                break        
    if stack:
        is_balanced = False

    if is_balanced:
        print("yes")
    else:
        print("no")


