import sys

def main():
    T = int(sys.stdin.readline().strip())

    for i in range(1,T+1):
        [K,C,S] = map(int, sys.stdin.readline().strip().split())
        lst = get_tile_list(K,C,S)
        print ("Case #%d: %s" % (i, lst))


def get_tile_list(k,c,s):
    
    if s==k:        
        lst = range(1,k+1)
        return " ".join(str(x) for x in lst)


    return "IMPOSSIBLE"


#calling main function
main()
