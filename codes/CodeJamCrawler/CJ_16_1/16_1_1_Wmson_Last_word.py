def last_word(word):
    cur_word = word[0]
    word = word [1:]
    for char in word:
        if cur_word[0] <= char:
            cur_word = char + cur_word
        else:
            cur_word = cur_word + char
    return cur_word

cases = int(raw_input())
for i in range(1,cases+1):
        word = raw_input()
        print("CASE #" + str(i) + ": " + str(last_word(word)))