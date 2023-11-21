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
            if not stack or stack[-1] != "(":
                is_balanced = False
                break
            stack.pop()    
        elif char == "]":
            if not stack or stack[-1] != "[":
                is_balanced = False
                break
            stack.pop()
                  
    if stack:
        is_balanced = False

    if is_balanced:
        print("yes")
    else:
        print("no")