def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        dictOfInts = {}
        INPUT = int(raw_input())
        j=0
        NEWINPUT = INPUT
        while len(dictOfInts)<10 and j<200:
            stringInput = str(NEWINPUT)
            for integer in stringInput:
                if (integer not in dictOfInts):
                    dictOfInts[integer] = 0
            j = j+1
            NEWINPUT = INPUT * j
        if j>=199:
            print "Case #{}: INSOMNIA".format(i)
        if len(dictOfInts)==10:
            print "Case #{}: {}".format(i, INPUT * (j-1))

    return 0
    
if __name__ == "__main__":
        main()