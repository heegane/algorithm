nums = input().split()
A = list(nums[0])
B = list(nums[1])

A[0], A[1], A[2] = int(A[2]), int(A[1]), int(A[0])
B[0], B[1], B[2] = int(B[2]), int(B[1]), int(B[0])

for i in range(3):
    if A[i] != B[i]:
        if A[i] > B[i]:
            print(''.join(map(str, A)))
            break
        else:
            print(''.join(map(str, B)))
            break
    else:
        continue
