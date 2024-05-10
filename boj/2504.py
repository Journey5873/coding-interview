input_str = input()
result = 0
num = 1
stack = []

for i in range(len(input_str)):

    if input_str[i] == "(":
        stack.append(input_str[i])
        num *= 2

    if input_str[i] == "[":
        stack.append(input_str[i])
        num *= 3
    
    if input_str[i] == ")":
        if input_str[i - 1] == "(":
            result += num
        if not stack or stack[-1] == "[":
            result = 0
            break
        stack.pop()
        num //= 2
    
    if input_str[i] == "]":
        if input_str[i - 1] == "[":
            result += num
        if  not stack or stack[-1] == "(":
            result = 0
            break
        stack.pop()
        num //= 3

if not stack:
    print(result)
else:
    print(0)