f = open('A-large.in', 'r')
output = open('AL.txt', 'w')

alpha = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,
         'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20,
         'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
number = int(f.readline())
string = [f.readline().strip('\n') for i in xrange(number)]


def put_letter(word, letter):
    if len(word) == 0:
        return [letter]

    if alpha[letter] < alpha[word[0]]:
        word.append(letter)
    else:word.insert(0, letter)
    return word


def solve(string):
    letters = [char for char in string]
    word = []

    for letter in letters:
        word = put_letter(word, letter)
    return ''.join(word)

for i in xrange(number):
    output.writelines('Case #{}: {}\n'.format(i+1, solve(string[i])))
    print 'Case #{}: {}'.format(i+1, solve(string[i]))
