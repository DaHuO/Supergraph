# Counting sheep module 1
"""
Bleatrix Trotter the sheep has devised a strategy that helps her fall asleep faster. First, she picks a number N. Then she starts naming N, 2 × N, 3 × N, and so on. Whenever she names a number, she thinks about all of the digits in that number. She keeps track of which digits (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen at least once so far as part of any number she has named. Once she has seen each of the ten digits at least once, she will fall asleep.

Bleatrix must start with N and must always name (i + 1) × N directly after i × N. For example, suppose that Bleatrix picks N = 1692. She would count as follows:

N = 1692. Now she has seen the digits 1, 2, 6, and 9.
2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
3N = 5076. Now she has seen all ten digits, and falls asleep.
What is the last number that she will name before falling asleep? If she will count forever, print INSOMNIA instead.
"""

def digitCounter(number):
    """function that returns a set of strings with the digits in a number"""
    full_set = {'0','1','2','3','4','5','6','7','8','9'}
    current_set = set()
    number_string = str(number)

    for digit in number_string:
        current_set.add(digit)
        if (full_set == current_set):
            break

    return current_set


def countSheep(seed):
    """
    function that accumulates the digits seen on starting with the seed, until the limit
    """

    full_set = {'0','1','2','3','4','5','6','7','8','9'}
    current_set = set()

    solution = False
    currentNumber = seed
    i = 1

    while(solution == False):
        inner_set = digitCounter(currentNumber)
        current_set = current_set | inner_set
        if (current_set == full_set):
            solution = currentNumber
        else :
            i += 1
            currentNumber = seed * i

    return solution


def caseRunner(file):
    resultfile = file+'.out'

    with open(file, 'r') as f:
        testcases = int(f.readline().rstrip('\n'))
        with open(resultfile, 'w') as rf:
            for i in range(testcases):
                case = f.readline().rstrip('\n')
                if case == '0' :
                    result = 'INSOMNIA'
                else :
                    result = countSheep(int(case))
                rf.write('Case #'+ str(i+1) +': ' + str(result) + '\n')
