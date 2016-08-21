def remove_letters(letters, word):
    for ch in word:
        del letters[letters.index(ch)]

t = int(raw_input())

for case in xrange(1,t+1):
    numbers = []
    letters = [x for x in raw_input()]
    #ZERO
    while 'Z' in letters:
        numbers.append(0)
        remove_letters(letters, 'ZERO')
    #TWO
    while 'W' in letters:
        numbers.append(2)
        remove_letters(letters, 'TWO')
    #FOUR
    while 'U' in letters:
        numbers.append(4)
        remove_letters(letters,'FOUR')
    #SIX
    while 'X' in letters:
        numbers.append(6)
        remove_letters(letters,'SIX')
    #EIGHT
    while 'G' in letters:
        numbers.append(8)
        remove_letters(letters,'EIGHT')
    #ONE
    while 'O' in letters:
        numbers.append(1)
        remove_letters(letters,'ONE')
    #THREE
    while 'T' in letters:
        numbers.append(3)
        remove_letters(letters,'THREE')
    #FIVE
    while 'F' in letters:
        numbers.append(5)
        remove_letters(letters,'FIVE')
    #SEVEN
    while 'S' in letters:
        numbers.append(7)
        remove_letters(letters,'SEVEN')
    #NINE
    while 'I' in letters:
        numbers.append(9)
        remove_letters(letters,'NINE')
    numbers.sort()
    print "Case #{}: {}".format(case, ''.join([str(x) for x in numbers]))
