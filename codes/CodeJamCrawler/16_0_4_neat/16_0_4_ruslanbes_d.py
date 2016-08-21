

def output(t, res):
    casestr = "Case #" + str(t+1) +": "
    status = str(res) if res != None else "IMPOSSIBLE"
    outputLine = casestr+status
    print outputLine


def main():
    T = int( raw_input() )

    for t in xrange(T):    
        K, C, S = map( int, raw_input().split(' ') )
        output(t, " ".join( map( str, xrange(1, S+1) ) ) )


if __name__ == "__main__":
   main()