text = input()
text_dict = {}

for char in text:
    if char not in text_dict:
        text_dict[char] = 0
    text_dict[char] += 1
text_dict = dict(sorted(text_dict.items(),key=lambda x :x[0]))

for key,value in text_dict.items():
    print(f'{key}: {value} time/s')