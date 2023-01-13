import collections

word = input()
if len(word) == 1:
    print(word.upper())
else:
    cnt = collections.Counter(word.upper()).most_common(2)

    if cnt[0][1] == cnt[1][1]:
        print("?")
    else:
        print(cnt[0][0])
