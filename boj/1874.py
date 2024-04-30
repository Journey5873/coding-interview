N = int(input())
input_arr = [int(input()) for _ in range(N)]
output_arr = []
stack = []
is_possible = True
last_number = 0

for number in input_arr:
    
    while last_number < number:
        last_number += 1
        stack.append(last_number)
        output_arr.append("+")

    if stack[-1] == number:
        stack.pop()
        output_arr.append("-")
    else:
        is_possible = False
        break

if is_possible:
    for element in output_arr:
        print(element)
else:
    print("NO")