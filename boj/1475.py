import sys

room_number = int(sys.stdin.readline())
digit_count = [0] * 10
max_count = 0

while room_number:
    digit_count[room_number%10] += 1
    room_number = room_number // 10

for i in range(digit_count):
    if i == 6 or i == 9:
        continue
    max_count = max(max_count, digit_count[i])

max_count = max((digit_count[6]+digit_count[9]+1)//2, max_count)