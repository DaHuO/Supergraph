
def checker():
    number_string = str(tocheck)
    for ch in number_string:
        sheep[int(ch)] = 1

def sleep():
    for k, v in sheep.iteritems():
        if (v == 0):
            return False

    return True

global input
global sheep

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
num_cases = int(raw_input())  # read a line with a single integer
for i in xrange(1, num_cases + 1):
    input = int(raw_input())#[int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    #print "Case #{}: {} {}".format(i, n + m, n * m)
    # check out .format's specification for more formatting options
    sheep = {0:0, 1: 0, 2: 0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    case = i
    done = False
    N = 1
    if(input == 0):
        tocheck = "INSOMNIA"
    else:
        while not done:
            tocheck = N*input
            checker()
            N+=1
            done = sleep()

    print "Case #{}:    {}".format(case, tocheck)
