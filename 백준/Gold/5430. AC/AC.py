import sys
from collections import deque

T = int(input())
isError = False

for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    nums = deque(sys.stdin.readline().rstrip().replace('[', '').replace(']', '').replace(',', ' ').split())

    count = 0
    for i in range(len(p)):
        if p[i] == 'R':
            count += 1
        else:
            if count % 2 == 0:
                if nums:
                    nums.popleft()
                else:
                    sys.stdout.write("error" + "\n")
                    isError = True
                    break
            else:
                if nums:
                    nums.pop()
                else:
                    sys.stdout.write("error" + "\n")
                    isError = True
                    break

    if not isError:
        if len(nums) == 0:
            sys.stdout.write("[]" + "\n")
        else:
            if count % 2 == 0:
                sys.stdout.write("[")
                for i in range(len(nums) - 1):
                    sys.stdout.write(str(nums[i]) + ",")
                sys.stdout.write(str(nums[-1]) + "]" + "\n")
            else:
                sys.stdout.write("[")
                for i in range(len(nums) - 1, 0, -1):
                    sys.stdout.write(str(nums[i]) + ",")
                sys.stdout.write(str(nums[0]) + "]" + "\n")

    nums.clear()
    isError = False
    count = 0
