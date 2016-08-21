

def main():
    fin = open('A-large.in','r')
    fout = open('output2.txt', 'w')

    cases = int(fin.readline())

    for i in range(cases):
        number = int(fin.readline().strip())

        result = getLastSheepNumber(number)

        output = "Case #{}: {}".format((i + 1), result)

        print output
        fout.write(output + '\n')


def getLastSheepNumber (initialint):

    a = set()
    curNum = initialint
    while len(a) < 10:
        if initialint == 0:
            ret = "INSOMNIA"
            break
        for x in map(int, str(curNum)):
            a.add(x)

        curNum += initialint
        ret = curNum - initialint
    return ret


if __name__ == '__main__':
	main()