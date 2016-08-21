from collections import Counter

digit_to_word = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

#letter_to_digit = {}
#for digit, word in enumerate(digit_to_word):
#    if digit in [0, 2, 4, 6, 8]:
#        continue
#    if digit in [1, 3, 5, 7]:
#        continue
#    if digit in [9]:
#        continue
#    for letter in word:
#        letter_to_digit.setdefault(letter, set()).add(digit)
#for letter, digits in letter_to_digit.items():
#    if len(digits) == 1:
#        print(letter, digits)

def solve():
    line = input()
    counts = Counter(line)
    ans = [0] * 10

    def sub(letter, digit):
        ans[digit] = counts[letter]
        for c in digit_to_word[digit]:
            counts[c] -= ans[digit]

    sub('Z', 0)
    sub('W', 2)
    sub('U', 4)
    sub('X', 6)
    sub('G', 8)

    sub('O', 1)
    sub('T', 3)
    sub('F', 5)
    sub('S', 7)

    sub('I', 9)

    solution = ''.join([str(digit) * count for digit, count in enumerate(ans)])
    sinput = ''.join(sorted(''.join(map(lambda d: digit_to_word[int(d)], solution))))
    realinput = ''.join(sorted(line))
    if sinput != realinput:
        print(line, solution)
        print(realinput)
        print(sinput)
        raise Exception()
    return solution

T = int(input())
for t in range(T):
    print('Case #{}: {}'.format(t + 1, solve()))
