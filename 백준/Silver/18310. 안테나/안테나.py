import sys

input = sys.stdin.readline

n = int(input())
locations = list(map(int, input().split()))
locations.sort()

sys.stdout.write(str(locations[(n - 1) // 2]) + "\n")