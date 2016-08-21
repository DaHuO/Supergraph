

def main():
    fin = open('B-large.in','r')
    fout = open('output2.txt', 'w')

    cases = int(fin.readline())

    for i in range(cases):
        test = (fin.readline().strip())

        result = combinations(test)
        output = "Case #{}: {}".format((i + 1), result)

        print output
        fout.write(output + '\n')

def combinations(seq):
    switches = 0
    result = 0

    if seq[0] == '-':
        result += 1

    for idx, val in enumerate(seq):
        for idx2, val2 in enumerate(seq):
            if idx2 - idx == 1 and val == '+' and val2 == '-':
                switches += 1



    result += switches * 2
    return result


if __name__ == '__main__':
	main()