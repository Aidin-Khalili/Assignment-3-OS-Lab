sentence = input('Please enter your sentence (to count it\'s words) : ').strip()
word_cnt = 1
for char in sentence:
    if char == ' ':
        word_cnt += 1
print('So it is : ', word_cnt)