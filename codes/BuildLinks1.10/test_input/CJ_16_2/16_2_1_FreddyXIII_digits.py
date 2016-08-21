from collections import Counter
ZERO = Counter("ZERO")
ONE = Counter("ONE")
TWO = Counter("TWO" )
THREE = Counter("THREE")
FOUR = Counter("FOUR")
FIVE = Counter("FIVE")
SIX = Counter("SIX")
SEVEN = Counter("SEVEN")
EIGHT = Counter("EIGHT")
NINE = Counter("NINE")

T = int(input())

for i in range(0,T):
    answer = []
    begin = input()
    keys =Counter(begin)
    fours = keys['U']
    zeroes = keys['Z']
    twos = keys['W']
    sixes = keys['X']
    eights = keys['G']
    for _ in range(0,fours):
        answer.append('4')
        keys = keys - FOUR
    for _ in range(0,zeroes):
        answer.append('0')
        keys = keys - ZERO
    for _ in range(0,twos):
        answer.append('2')
        keys = keys - TWO
    for _ in range(0,sixes):
        answer.append('6')
        keys = keys - SIX
    for _ in range(0,eights):
        answer.append('8')
        keys = keys - EIGHT
    threes = keys['R']
    fives = keys['F']
    sevens = keys['S']
    for _ in range(0,threes):
        answer.append('3')
        keys = keys - THREE
    for _ in range(0,fives):
        answer.append('5')
        keys = keys - FIVE
    for _ in range(0,sevens):
        answer.append('7')
        keys = keys - SEVEN
    ones = keys['O']
    nines = keys['I']
    for _ in range(0, ones):
        answer.append('1')
    for _ in range(0,nines):
        answer.append('9')
    result = ''.join(sorted(answer))
    print("Case #" + str(i+ 1) + ": " + result)
