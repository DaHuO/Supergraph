def solution():
    word = input()
    new_word = word[0]
    for char in word[1:]:
        if char >= new_word[0]:
            new_word = char + new_word
        else:
            new_word += char
    return new_word

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        print("Case #{}: {}".format(i, solution()))
