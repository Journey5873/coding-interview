T = int(input())

# 0: N, 1: S, 2: E, 3: W

for _ in range(T):
    commands = list(input().strip())
    x, y, direction = 0, 0, 0
    min_x, max_x = 0, 0
    min_y, max_y = 0, 0

    for c in commands:

        if c == "F":
            if direction == 0:
                y += 1
            if direction == 1:
                y -= 1
            if direction == 2:
                x += 1
            if direction == 3:
                x -= 1

        if c == "B":
            if direction == 0:
                y -= 1
            if direction == 1:
                y += 1
            if direction == 2:
                x -= 1
            if direction == 3:
                x += 1
        
        if c == "L":
            if direction == 0:
                direction = 3
            elif direction == 1:
                direction = 2
            elif direction == 2:
                direction = 0
            elif direction == 3:
                direction = 1
        
        if c == "R":
            if direction == 0:
                direction = 2
            elif direction == 1:
                direction = 3
            elif direction == 2:
                direction = 1
            elif direction == 3:
                direction = 0

        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)


    width = abs(max_x - min_x)
    height = abs(max_y - min_y)
    area = width * height

    print(area)