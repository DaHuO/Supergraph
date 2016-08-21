def output(t, res):
    casestr = "Case #" + str(t+1) +": "
    status = str(res) if res != None else "INSOMNIA"
    outputLine = casestr+status
    print outputLine



def main():
    T = int( raw_input() )

    for t in xrange(T):    
        N = raw_input()
        digits = set(N)
        N = int(N) 
        if N == 0:
            output(t, None)
            continue

        lastN = N
        while len(digits) < 10:
            lastN += N
            digits.update(set(str(lastN)))            

        output(t, lastN)

if __name__ == "__main__":
   main()