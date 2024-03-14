import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    sound = list(input().split())
    while True:
        data = input().rstrip()
        if data == 'what does the fox say?':
            print(' '.join(sound))
            break
        else:
            data = list(data.split())[2]
            while data in sound:
                sound.remove(data)
