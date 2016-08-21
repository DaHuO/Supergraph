# GCJ 2016 A-small

infile = open("A-large.in", "r")
outfile = open("A-large-result.txt", "w")

T = int(infile.readline())
for case in range(T):
    N = int(infile.readline())

    if N == 0:
        outfile.write("Case #{0}: INSOMNIA\n".format(str(case + 1)))

    else:
        i = 1

        digits = []
        while len(digits) < 10:
            number = str(N * i)
            for j in range(len(number)):
                if number[j] not in digits:
                    digits.append(number[j])
            i += 1

        outfile.write("Case #{0}: {1}\n".format(str(case + 1), str((N * (i -1)))))
    


infile.close()
outfile.close()
