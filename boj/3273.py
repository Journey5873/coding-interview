n = int(input())
numsArr = list(map(int, input().split()))
target = int(input())

cnt = 0
dic = {}
for num in numsArr:
    diff = target - num
    if diff in dic:
        cnt += 1
    dic[num] = True
print(cnt)