from collections import defaultdict

n = int(input())
numbers = list(map(int, input().split()))
target = int(input())
visited = defaultdict(bool)
count = 0

for num in numbers:
    diff = target - num
    count += visited[diff]
    visited[num] = True
    
print(count)