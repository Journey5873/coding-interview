input_string = input()
stack = []

laser = 0
result = 0
for i in range(len(input_string)):
    if input_string[i] == "(":
        stack.append("(")
    else:
        if input_string[i - 1] == "(":
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)