
global input
global sheep

def checker():
    number_string = str(numtocheck)
    for ch in number_string:
        sheep[int(ch)] = 1

def toSleep():
    for key, value in sheep.iteritems():
        if (value == 0):
            return False

    return True


nums = int(raw_input())
for i in xrange(1, nums + 1):
    input = int(raw_input())

    sheep = {0:0, 1: 0, 2: 0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    num = i
    done = False
    N = 1
    if(input == 0):
        numtocheck = "INSOMNIA"
    else:
        while not done:
            numtocheck = N*input
            checker()
            N+=1
            done = toSleep()

    print "Case #{}:    {}".format(num, numtocheck)
