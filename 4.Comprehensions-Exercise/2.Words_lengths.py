words = [word for word in input().split(', ')]
i = 0
for word in words:
    words[i] = f'{word} -> {len(word)}'
    i += 1
print(', '.join(words))