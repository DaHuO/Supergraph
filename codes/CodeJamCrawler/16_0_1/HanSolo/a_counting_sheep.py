

def solve_case(n):
    if n == 0:
        return 'INSOMNIA'

    digits = [False for x in range(10)]

    remaining = 10

    sheep_no = 0
    while remaining > 0:
        sheep_no += 1

        new_n = sheep_no * n

        str_n = str(new_n)

        for c in str_n:
            d = int(c)
            if not digits[d]:
                remaining -= 1
                digits[d] = True

        if remaining <= 0:
            return str(new_n)


# start
infile = open('A-large'+'.in', 'r')
outfile = open('A-large'+'.out', 'w')

T = int(infile.readline().strip())

for ti in range(T):
    N = int(infile.readline().strip())

    soln = solve_case(N)

    outfile.write('Case #'+str(ti+1)+': '+soln+'\n')

infile.close()
outfile.close()




