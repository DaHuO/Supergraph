from collections import namedtuple, defaultdict
import sys


def run(N):
    suite = set(str(N))
    sign = []
    loops = [-1]

    i = 0

    while True:
        i += 1
        #print "i: ", i
        numb = i*N

        if len(suite) == 10:
            return (i-1)*N

        if len(loops)-1 == len(str(numb)):
            #print 'insom ', suite, loops, numb, len(loops)-1, len(str(numb))
            return "INSOMNIA"

        for idx, c in enumerate(str(numb)[::-1]):
            #print "numb: %s, idx:%s, c:%s, l:%s, s:%s" % (numb, idx, c, loops, sign)
            if idx in loops:
                continue
            if idx-1 in loops:
                rest_i = i%10
                s = "%s:%s:%s" % (idx, c, rest_i)
                #print '(s) ', s
                if s not in sign:
                    sign.append(s)
                else:
                    loops.append(idx)
                    
            else:
                break
        suite = suite.union(str(numb))
        #print "numb: ", numb



def start():
    T = sys.stdin.readline()
    # T=1
    case = 0
    for i in xrange(int(T)):
        case += 1
        line = sys.stdin.readline()
        
        N = int( line.strip() )
        out =  run(N)

        print "Case #%s: %s" % (case, out)

if __name__ == "__main__":
    start()