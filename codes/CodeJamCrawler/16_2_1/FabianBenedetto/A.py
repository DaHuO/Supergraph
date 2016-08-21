str1 = 'ONE'
str2 = 'TWO'
str3 = 'THREE'
str4 = 'FOUR'
str5 = 'FIVE'
str6 = 'SIX'
str7 = 'SEVEN'
str8 = 'EIGHT'
str9 = 'NINE'
str0 = 'ZERO'


def mainfunc(numstr,i):
    number = list()
    numlist = list()
    for letter in numstr:
        numlist.append(letter)

    n = numlist.count('X')
    for _ in range(n):
        number.append(6)
        for let in str6:
            numlist.remove(let)

    n = numlist.count('W')
    for _ in range(n):
        number.append(2)
        for let in str2:
            numlist.remove(let)

    n = numlist.count('S')
    for _ in range(n):
        number.append(7)
        for let in str7:
            numlist.remove(let)

    n = numlist.count('Z')
    for _ in range(n):
        number.append(0)
        for let in str0:
            numlist.remove(let)

    n = numlist.count('V')
    for _ in range(n):
        number.append(5)
        for let in str5:
            numlist.remove(let)

    n = numlist.count('F')
    for _ in range(n):
        number.append(4)
        for let in str4:
            numlist.remove(let)

    n = numlist.count('O')
    for _ in range(n):
        number.append(1)
        for let in str1:
            numlist.remove(let)

    n = numlist.count('G')
    for _ in range(n):
        number.append(8)
        for let in str8:
            numlist.remove(let)

    n = numlist.count('R')
    for _ in range(n):
        number.append(3)
        for let in str3:
            numlist.remove(let)

    n = numlist.count('I')
    for _ in range(n):
        number.append(9)
        for let in str9:
            numlist.remove(let)

    number = sorted(number)
    return "Case #" + str(i) + ": " + "".join(str(e) for e in number)



t = int(raw_input())
for i in xrange(1, t + 1):
    mystr = raw_input()
    print mainfunc(mystr,i)
