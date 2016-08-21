if __name__ == "__main__":

    #fin = open('A-small-attempt0.in', 'r')
    #fout = open('A-small-attempt0.out', 'w')

    fin = open('A-large.in', 'r')
    fout = open('A-large.out', 'w')

    cases = int(fin.readline())
    print cases

    for t in range(0, cases):
        s = ''
        n = int(fin.readline())
        if n == 0:
            s = "INSOMNIA"
        else:
            n2 = n
            digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            while len(digits) != 0:
                new_digits = []
                for i in range(0, len(digits)):
                    if digits[i] not in str(n2):
                        new_digits.append(digits[i])
                digits = new_digits
                if len(digits) != 0:
                    n2 += n
            s = str(n2)

        print "Case #%d: %s" % (t+1, s)
        fout.write("Case #" + str(t+1) + ": " + s + "\n")

    fin.close()
    fout.close()