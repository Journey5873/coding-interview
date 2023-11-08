n = int(input())
numbers = list(map(int, input().split()))
target = int(input())

count = 0
visited = {}
for num in numbers:
    diff = target - num
    if diff in visited:
        count += 1
    visited[num] = True
print(count)