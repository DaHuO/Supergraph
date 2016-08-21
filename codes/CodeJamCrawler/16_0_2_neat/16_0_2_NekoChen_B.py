import sys

def solve( s ):
    x = len( filter( None, s.split("+") ) )
    if x == 0: return 0
    if s[0] == '+': return x+x
    return x + x - 1

def main():
    f = open( sys.argv[1] )
    #f = sys.stdin
    T = int(f.next())
    for case in range(1,T+1):
        print "Case #{0}: {1}".format( case, solve( f.next().strip() ) )

if __name__ == "__main__":
    main()
