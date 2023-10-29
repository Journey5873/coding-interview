roomNumber = int(input())
numberArr = [0] * 10

while roomNumber:
    numberArr[roomNumber%10] += 1
    roomNumber = roomNumber // 10

numberCount = 0
for i in range(len(numberArr)):
    if i == 6 or i == 9:
        continue
    else:
        numberCount = max(numberCount, numberArr[i])

numberCount = max(numberCount, (numberArr[6] + numberArr[9] + 1) // 2)
print(numberCount)