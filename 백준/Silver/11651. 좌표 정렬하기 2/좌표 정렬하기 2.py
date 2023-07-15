import sys

N = int(input())
points = []

for _ in range(N):
    input_data = sys.stdin.readline().rstrip().split()
    x, y = int(input_data[0]), int(input_data[1])
    points.append([x, y])

points.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    sys.stdout.write(str(points[i][0]) + " " + str(points[i][1]) + "\n")
