word = input()
word = word.replace('c=', '!').replace('c-', '!').replace('dz=', '!').replace('d-', '!').replace('lj', '!').replace(
    'nj', '!').replace('s=', '!').replace('z=', '!')
print(len(word))
