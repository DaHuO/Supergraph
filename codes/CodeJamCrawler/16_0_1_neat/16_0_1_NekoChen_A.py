import sys

def digits( x ):
    while (x):
        yield x % 10
        x /= 10

def solve( N ):
    if N == 0: return "INSOMNIA"
    x = 0
    hit = [ False ]*10
    hitcount = 0
    while hitcount < 10:
        #print "x=", x
        x += N
        for i in digits(x):
            #print "digit:", i
            if hit[i]: continue
            hit[i] = True
            hitcount += 1
    return x

def main():
    f = open( sys.argv[1] )
    #f = sys.stdin
    T = int(f.next())
    for case in range(1,T+1):
        print "Case #{0}: {1}".format( case, solve( int(f.next()) ) )

if __name__ == "__main__":
    main()
