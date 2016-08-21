T = int(input())

def check_elim(S, chars):
    rem = S
    for char in chars:
        rem = rem.replace(char, '', 1)

    if len(rem) + len(chars) == len(S):
        return rem
    else:
        return None

def find(S, number):
    # print(S)
    zero = check_elim(S, 'ZERO')
    one = check_elim(S, 'ONE')
    two = check_elim(S, 'TWO')
    three = check_elim(S, 'THREE')
    four = check_elim(S, 'FOUR')
    five = check_elim(S, 'FIVE')
    six = check_elim(S, 'SIX')
    seven = check_elim(S, 'SEVEN')
    eight = check_elim(S, 'EIGHT')
    nine = check_elim(S, 'NINE')

    if zero != None:
        if len(zero) == 0:
            return number + '0'
        found = find(zero, number + '0')
        if found != None:
            return found
    if one != None:
        if len(one) == 0:
            return number + '1'
        found = find(one, number + '1')
        if found != None:
            return found
    if two != None:
        if len(two) == 0:
            return number + '2'
        found = find(two, number + '2')
        if found != None:
            return found
    if three != None:
        if len(three) == 0:
            return number + '3'
        found = find(three, number + '3')
        if found != None:
            return found
    if four != None:
        if len(four) == 0:
            return number + '4'
        found = find(four, number + '4')
        if found != None:
            return found
    if five != None:
        if len(five) == 0:
            return number + '5'
        found = find(five, number + '5')
        if found != None:
            return found
    if six != None:
        if len(six) == 0:
            return number + '6'
        found = find(six, number + '6')
        if found != None:
            return found
    if seven != None:
        if len(seven) == 0:
            return number + '7'
        found = find(seven, number + '7')
        if found != None:
            return found
    if eight != None:
        if len(eight) == 0:
            return number + '8'
        found = find(eight, number + '8')
        if found != None:
            return found
    if nine != None:
        if len(nine) == 0:
            return number + '9'
        found = find(nine, number + '9')
        if found != None:
            return found
    return None

def solve():
    S = input()
    return find(S, '')

for t in range(T):
    print('Case #' + str(t+1) + ': ' + solve())
