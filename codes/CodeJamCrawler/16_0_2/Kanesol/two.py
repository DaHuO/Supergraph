
def flipit(indx):
    x=0
    for i in input:
        #print i + input[x]
        if(input[x] == "+"):
            input[x] = "-"
        elif(input[x] == "-"):
            input[x] = "+"
        x+=1
        #print "Iteration {} is {}".format(x, "".join(input))


global input
global sheep

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
num_cases = int(raw_input())  # read a line with a single integer
for i in xrange(1, num_cases + 1):
    input = str(raw_input())#[int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    #print "Case #{}: {} {}".format(i, n + m, n * m)
    # check out .format's specification for more formatting options
    #print "Original: "+input
    #test Code
    #input = "--"
    #case = 1
    length = len(input)
    input = list(input[::-1])
    #print "Reversed: "+"".join(input)
    case = i
    done = False
    N = 0
    count_flips = 0
    #print input

    while N < length:
        if(input[N] == "-"):
            flipit(N)
            count_flips +=1
            #print "".join(input)

        N+=1



    print "Case #{}:    {}".format(case, count_flips)
