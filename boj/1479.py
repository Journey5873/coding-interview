h, w = map(int, input().split())
blocks = list(map(int, input().split()))
rain = 0

for i in range(1, len(blocks)-1):
    left = max(blocks[:i])
    right = max(blocks[i+1:])
    lower_bolock = min(left, right)

    if blocks[i] < lower_bolock:
        rain += lower_bolock - blocks[i]

print(rain)