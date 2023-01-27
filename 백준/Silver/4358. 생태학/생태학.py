import sys

tree = {}
trees = 0
while True:
    data = sys.stdin.readline().rstrip()
    if not data:
        break
    else:
        if data in tree:
            tree[data] += 1
        else:
            tree[data] = 1
    trees += 1

tree = sorted(tree.items(), key=lambda x: x[0])
n = len(tree)

for i in range(n):
    print("%s %.4f" % (tree[i][0], (int(tree[i][1]) / trees) * 100))
