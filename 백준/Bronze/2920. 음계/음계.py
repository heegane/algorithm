import sys

num = list(map(int, sys.stdin.readline().split()))
correct_a = 0
correct_d = 0

for i in range(0, 8):
    if num[0] != 1 and num[0] != 8:
        break

    else:
        if num[i] == i + 1:
            correct_a += 1
        elif num[i] == 8 - i:
            correct_d += 1
        else:
            break

if correct_a == 8:
    print("ascending")
elif correct_d == 8:
    print("descending")
else:
    print("mixed")
