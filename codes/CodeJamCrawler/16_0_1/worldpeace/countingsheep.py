f = open('A-large.in', 'r')

# Extract the input
T = int(f.next())
cases = [int(f.next()) for x in range(T)]  # [0, 1, 2, 11, 1692]

f.close()

o = open('output.txt', 'w')

for i, case in enumerate(cases):

    numList = [_ for _ in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    j = 0

    while len(numList) > 0:

        N = (j + 1) * case

        for n in str(N):

            if int(n) in numList:
                numList.remove(int(n))

        j += 1

        if j == 1000:  # All tested cases were solved in 72 or less attempts
            N = "INSOMNIA"
            break

    o.write("Case #%s: %s\n" % (i + 1, str(N)))

o.close()
