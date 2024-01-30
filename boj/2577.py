A = int(input())
B = int(input())
C = int(input())

product = A * B * C
num_arr = [0] * 10

for digit in str(product):
    num_arr[int(digit)] += 1

for count in num_arr:
    print(count)