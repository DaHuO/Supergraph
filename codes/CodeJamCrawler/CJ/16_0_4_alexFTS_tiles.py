import sys

def tiles(l):
    k,c,s = l.split(' ')
    k = int(k)
    s = int(s)
    
    if k > s:
        imp = "IMPOSSIBLE"
        return imp
    else:
        return ' '.join(map(str, range(1, k+1)))
            
    
def main():
    if len(sys.argv) != 1:
        sys.exit('Usage: python program.py < input')
    
    i = 1
    maximum = int(sys.stdin.readline())
    
    for l in sys.stdin:
        if i > maximum:
            break
            
        print "Case #%i: " %i + tiles(l)
        i += 1
    return

if __name__ == '__main__':
    main()
