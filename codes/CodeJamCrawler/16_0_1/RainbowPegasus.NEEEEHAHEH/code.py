def findLast(N):
    d = {}
    if N == 0:
        outp.write("Case #" + str(case+1) + ": INSOMNIA" + '\n')
    else:
        i = 1
        current = 0
        while len(d) != 10:
            current = i*N
            for each_digit in str(current):
                d[each_digit] = d.get(each_digit, 0) + 1 
            i += 1
        outp.write("Case #" + str(case+1) + ": " + str(current) + '\n')

        
inp = open('A-small-attempt0.in', 'r')
outp = open('output', 'w+')
test_cases = int(inp.readline())
for case in range(test_cases):
    N = int(inp.readline())
    findLast(N)