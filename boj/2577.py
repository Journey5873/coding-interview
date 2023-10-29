A = int(input())
B = int(input())
C = int(input())

product = A * B * C
numsArr = [0] * 10
while product:
    numsArr[product%10] += 1
    product = product // 10

for i in range(len(numsArr)):
    print(numsArr[i])