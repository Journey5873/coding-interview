S = input()
alpha = [0] * 26

for c in S:
    alpha[ord(c) - ord('a')] += 1

print(*alpha)