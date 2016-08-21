infile = open("A-large.in")
outfile = open("output.txt", 'w')

T = infile.readline()
T = int(T[:-1])

for x in range(1, T+1):
    N = infile.readline()
    N = int(N[:-1])

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    if N == 0:
        outfile.write("Case #%s: INSOMNIA\n" % x)
    else:
        i = 1
        while len(numbers) != 0:
            temp = str(i * N)

            for each in temp:
                each = int(each)
                if each in numbers:
                    numbers.remove(each)

            i += 1
        outfile.write("Case #%s: %s\n" % (x, temp))

infile.close()
outfile.close()