


zero = ['E','R','O']
six = ['I','S']
two = ['T','O']
eight = ['E','I','H','T']
seven = ['E','E','N']
five = ['F','I','E']
four = ['O','U','R']
three = ['T','R','E','E']
nine  = ['N','N','E']


def find_phone(number):
    number = list(number)
    ans = []
    while len(number) > 0 and 'Z' in number:
        number.remove('Z')
        ans.append('0')
        for i in range(len(zero)):
            number.remove(zero[i])

    while len(number) > 0 and 'W' in number:
        number.remove('W')
        ans.append('2')
        for i in range(len(two)):
            number.remove(two[i])

    while len(number) > 0 and 'X' in number:
        number.remove('X')
        ans.append('6')
        for i in range(len(six)):
            number.remove(six[i])

    while len(number) > 0 and 'G' in number:
        number.remove('G')
        ans.append('8')
        for i in range(len(eight)):
            number.remove(eight[i])

    while len(number) > 0 and 'S' in number and 'V' in number:
        number.remove('S')
        number.remove('V')
        ans.append('7')
        for i in range(len(seven)):
            number.remove(seven[i])

    while len(number) >0 and 'V' in number:
        number.remove('V')
        ans.append('5')
        for i in range(len(five)):
            number.remove(five[i])

    while len(number) >0 and 'F' in number:
        number.remove('F')
        ans.append('4')
        for i in range(len(four)):
            number.remove(four[i])

    while len(number) >0 and 'H' in number:
        number.remove('H')
        ans.append('3')
        for i in range(len(three)):
            number.remove(three[i])

    while len(number)>0 and 'I' in number:
        number.remove('I')
        ans.append('9')
        for i in range(len(nine)):
            number.remove(nine[i])

    if len(number) > 0 :
        count = len(number) /3
        for i in range(count):
            ans.append('1')

    return "".join(sorted(ans))

for i in range(1,input()+1):
    number = raw_input()
    print "Case #{0}: {1}".format(i,find_phone(number))