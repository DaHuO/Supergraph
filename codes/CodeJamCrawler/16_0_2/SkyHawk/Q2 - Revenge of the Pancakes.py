infile = open("B-large.in")
outfile = open("output.txt", 'w')

T = infile.readline()
T = int(T[:-1])

keys = {}
chain = '-'

for i in range(1, 101):
    keys[chain] = len(chain)

    if i % 2 != 0:
        chain = '+' + chain
    else:
        chain = '-' + chain

for x in range(1, T+1):
    S = infile.readline()
    S = S[:-1]

    string = S[0]

    for each in S[1:]:
        if string[-1] == each:
            pass
        else:
            string += each

    if string == '+':
        outfile.write("Case #%s: 0\n" % x)
    else:
        if string[-1] == '+':
            string = string[:-1]

        outfile.write("Case #%s: %s\n" % (x, keys[string]))