import sys

n = int(sys.stdin.readline())
moneys = []

for _ in range(n):
    money = int(sys.stdin.readline())
    if money == 0 and moneys:
        moneys.pop()
    else:
        moneys.append(money)

total = sum(moneys)
print(total)