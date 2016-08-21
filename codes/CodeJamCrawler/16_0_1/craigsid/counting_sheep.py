import sys
import string

fname = sys.argv[1]

# Check numbers seen
fa = [False, False, False, False, False, False, False, False, False, False]
def resetNumbers():
    for i in range(len(fa)):
        fa[i] = False

def gotNumber(n):
    fa[n] = True;

def allNumbersFound():
    # Check if we've got all the numbers
    for f in fa:
        if not f:
            return False

    return True

with open(fname) as f:
    # T - number of test cases
    T = int(string.split(f.readline())[0])
    #print "T {}".format(T)

    for t in range(T):
        # N - starting number as a string
        N = int(string.split(f.readline())[0])
        #print "N {}".format(N)

        # If 0 then insomnia - are there other inputs?
        if N == 0:
            print("Case #{}: INSOMNIA".format(t+1))

        else:
            # spin round until we've found them all
            resetNumbers()
            i = 1
            found = False
            while not found:
                m = N * i
                #print "m {}".format(m)
                for  n in str(m):
                    #print "n: {}".format(n)
                    gotNumber(int(n))

                if (allNumbersFound()):
                    print "Case #{}: {}".format(t+1, m)
                    found = True

                i += 1


                


