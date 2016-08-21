def last_word(s):
    word_list = [s[0]]
    for char in s[1:]:
        if char >= word_list[0]:
            word_list.insert(0, char)
        else:
            word_list.append(char)
    return ''.join(word_list)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print('Case #{}: {}'.format(i + 1, last_word(s)))
