import sys

def solve( K, C, S ):
    s = 0
    k = 1
    for i in range(C):
        s += k
        k *= K        
    return " ".join( map( str, [ i*s+1 for i in range(K) ] ) )

def main():
    f = open( sys.argv[1] )
    #f = sys.stdin
    T = int(f.next())
    for case in range(1,T+1):
        print "Case #{0}: {1}".format( case, solve( *map(int, f.next().strip().split() ) ) )

if __name__ == "__main__":
    main()
