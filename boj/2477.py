K = int(input())

arr = [list(map(int, input().split())) for _ in range(6)]

max_height = max_width = 0
bigger_box = smaller_box = 1
for i in range(6):

    if arr[i][0] == 3 or arr[i][0] == 4:
        max_height = max(arr[i][1], max_height)
    if arr[i][0] == 1 or arr[i][0] == 2:
        max_width = max(arr[i][1], max_width)

    next = (i + 1) % 6
    nnext = (i + 2) % 6
    if arr[i][0] == arr[nnext][0]:
        smaller_box *= arr[next][1]

bigger_box = (max_height * max_width) - smaller_box
print(bigger_box * K)