import sys

n = int(sys.stdin.readline())
operators = []
stack = []

last_num = 1
is_possible = True
for _ in range(n):
    intput_num = int(sys.stdin.readline())

    for i in range(last_num, intput_num+1):
        operators.append("+")
        stack.append(i)
        last_num += 1

    if (stack[-1] == intput_num):
        operators.append("-")
        stack.pop()
    else:
        is_possible = False
        break
    
if is_possible:
    for operator in operators:
        print(operator)
else:
    print("NO")