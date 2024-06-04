import sys
input = sys.stdin.readline

arr = input().strip()

def solution():
    stack = []
    result = 0

    for i in range(len(arr)):
        if arr[i] == "(":
            stack.append("(")
        elif arr[i] == ")" and arr[i-1] == "(":
            stack.pop()
            result += len(stack)
        elif arr[i] == ")" and arr[i-1] == ")":
            stack.pop()
            result += 1
    return result

print(solution())