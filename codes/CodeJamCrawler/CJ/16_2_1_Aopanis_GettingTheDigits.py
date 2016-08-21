o = open("C:\Users\ANTON\Downloads\A-large (1).in")
w = open("C:\Users\ANTON\PycharmProjects\CodeJam\Round1B\GettingTheDigits\Large-Output.txt", 'w')

tests = [i.strip('\n').lower() for i in o]
number_test = tests.pop(0)

for index, test in enumerate(tests):
    letters = [i for i in test]
    print letters
    solution = []
    while letters:
        for i in range(len(letters)):
            if 'z' in letters:
                letters.remove('z')
                letters.remove('e')
                letters.remove('r')
                letters.remove('o')
                solution.append(0)
            if 'w' in letters:
                letters.remove('t')
                letters.remove('w')
                letters.remove('o')
                solution.append(2)
            if 'u' in letters:
                letters.remove('f')
                letters.remove('o')
                letters.remove('u')
                letters.remove('r')
                solution.append(4)
            if 'x' in letters:
                letters.remove('s')
                letters.remove('i')
                letters.remove('x')
                solution.append(6)
            if 'g' in letters:
                letters.remove('e')
                letters.remove('i')
                letters.remove('g')
                letters.remove('h')
                letters.remove('t')
                solution.append(8)
        for i in range(len(letters)):
            if 'h' in letters:
                letters.remove('t')
                letters.remove('h')
                letters.remove('r')
                letters.remove('e')
                letters.remove('e')
                solution.append(3)
            if 's' in letters:
                letters.remove('s')
                letters.remove('e')
                letters.remove('v')
                letters.remove('e')
                letters.remove('n')
                solution.append(7)
            if 'o' in letters:
                print letters
                letters.remove('o')
                letters.remove('n')
                letters.remove('e')
                solution.append(1)
            if 'f' in letters:
                letters.remove('f')
                letters.remove('i')
                letters.remove('v')
                letters.remove('e')
                solution.append(5)

        if 'n' in letters:
            letters.remove('n')
            letters.remove('i')
            letters.remove('n')
            letters.remove('e')
            solution.append(9)

    number = ''.join([str(i) for i in sorted(solution)])
    print number
    w.write("Case #" + str(index + 1) + ': ' + number + '\n')
