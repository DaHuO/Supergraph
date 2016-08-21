import sys

def main():

    try:
        fileSize = sys.argv[1]

    except IndexError:
        fileSize = 'small'



    r_file = open('A-' + fileSize + '.in','r')
    w_file = open('sheep_out.txt','w')

    t = int(r_file.readline())

    for x in range(t):

        n = int(r_file.readline())

        outputString = 'Case #{x}: {y}\n'.format(x = x + 1, y = sheep(n))

        w_file.write(outputString)

    r_file.close(); w_file.close()

def sheep(n):

    digitsSeen = []
    numbersSeen = []

    multiplier = 0
    while len(digitsSeen) != 10: # while all digits have not been seen

        if multiplier > 105: return 'INSOMNIA'
        multiplier += 1

        newNumber = n * multiplier
        #print newNumber
        for digit in str(newNumber):

            if digit not in digitsSeen:
                digitsSeen += digit

    return newNumber

if __name__ == '__main__':
    main()


