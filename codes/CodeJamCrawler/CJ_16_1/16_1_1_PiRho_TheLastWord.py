def get_last_word(word):
    last_word = ''
    for letter in word:
        # Base case
        if last_word == '':
            last_word = str(letter)
            continue
        if last_word[0:1]>letter:
            last_word = last_word + letter
        else:
            last_word = letter + last_word
    return last_word

file = open('A-large.in','r')
output_file = open('output.txt','w')
n = int(file.readline())
i = 0

while i < n:
    word = file.readline().strip()
    word = get_last_word(word)
    print 'Case #' + str(i+1) + ': ' + word
    output_file.write('Case #' + str(i+1) + ': ' + word + '\n')
    i += 1