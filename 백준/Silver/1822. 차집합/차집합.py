import sys

nA, nB = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_element = {}

for i in range(nA):
    if A[i] not in A_element:
        A_element[A[i]] = i

for i in range(nB):
    if B[i] in A_element:
        del A_element[B[i]]

if len(A_element) == 0:
    sys.stdout.write("0\n")

else:
    A_element = sorted(A_element.items(), key=lambda x: x[0])
    cnt = 1
    sys.stdout.write(str(len(A_element)) + "\n")
    for element in A_element:
        if cnt == len(A_element):
            sys.stdout.write(str(element[0]))
            break
        else:
            sys.stdout.write(str(element[0]) + " ")
            cnt += 1
