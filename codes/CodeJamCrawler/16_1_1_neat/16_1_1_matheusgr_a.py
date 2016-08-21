import sys

# disable before commit:
#f_name = 'base.txt'
#f_name = 'small.txt'
f_name = 'large.txt'
sys.stdin = open(f_name)

# disable to test:
sys.stdout = open('output.txt', 'w')
cases = int(input())

for case in range(cases):
    letters = input()
    word = letters[0]
    for letter in letters[1:]:
        if ord(letter) >= ord(word[0]):
            word = letter + word
        else:
            word += letter
    print("Case #%i: %s" % (case + 1, word))
