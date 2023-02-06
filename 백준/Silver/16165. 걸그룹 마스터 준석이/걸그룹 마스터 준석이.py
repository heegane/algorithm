import sys

N, M = map(int, input().split())
girl_group = {}

for _ in range(N):
    group_name = sys.stdin.readline().rstrip()
    group_nums = int(sys.stdin.readline().rstrip())
    for _ in range(group_nums):
        member_name = sys.stdin.readline().rstrip()
        girl_group[member_name] = group_name

girl_group = sorted(girl_group.items())
girl_group_dic = dict(girl_group)

for _ in range(M):
    question = sys.stdin.readline().rstrip()
    q_type = int(sys.stdin.readline().rstrip())

    if q_type == 0:
        for member in girl_group:
            if member[1] == question:
                sys.stdout.write(member[0] + "\n")

    if q_type == 1:
        sys.stdout.write(girl_group_dic[question] + "\n")
