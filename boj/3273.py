N = int(input())
input_arr = list(map(int, input().split()))
target = int(input())
visited = {}
count = 0

for i in range(N):
    diff = target - input_arr[i]
    if diff in visited:
        count += 1
    visited[input_arr[i]] = True

print(count)