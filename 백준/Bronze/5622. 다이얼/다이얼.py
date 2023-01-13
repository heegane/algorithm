word = input()
result = 0

for i in range(len(word)):
    if word[i] == 'A' or word[i] == 'B' or word[i] == 'C':
        result += 3
    elif word[i] == 'D' or word[i] == 'E' or word[i] == 'F':
        result += 4
    elif word[i] == 'G' or word[i] == 'H' or word[i] == 'I':
        result += 5
    elif word[i] == 'J' or word[i] == 'K' or word[i] == 'L':
        result += 6
    elif word[i] == 'M' or word[i] == 'N' or word[i] == 'O':
        result += 7
    elif word[i] == 'P' or word[i] == 'Q' or word[i] == 'R' or word[i] == 'S':
        result += 8
    elif word[i] == 'T' or word[i] == 'U' or word[i] == 'V':
        result += 9
    else:
        result += 10

print(result)
