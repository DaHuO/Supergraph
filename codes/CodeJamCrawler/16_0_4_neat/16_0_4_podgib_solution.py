input = open('D-small-attempt0.in', 'r')
output = open('D-small-attempt0.out', 'w')

T = int(input.readline().strip())

for X in range(1,T+1):
    tokens = input.readline().strip().split(' ')
    K = int(tokens[0])
    C = int(tokens[1])
    S = int(tokens[2])

    print "Case #" + str(X) + ":",
    output.write("Case #" + str(X) + ":")
    for i in range(1,S+1):
        print " " + str(i),
        output.write(" " + str(i))
    print ""
    output.write("\n")
