import sys
sys.setrecursionlimit(10000)

def read_line(f):
    while True:
        s=f.readline().strip()
        if s:
            return s
def read_list(f):
    return [int(x) for x in read_line(f).split()]
def read_tuple(f):
    return tuple(read_list(f))

def load_single_case(f):
    return read_tuple(f)


def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
            cases.append(load_single_case(f))
    return cases



winp={"RP":"P","PR":"P",
      "SR":"R","RS":"R",
      "PS":"S","SP":"S"}
def red(s):
    if len(s)<2:
        return True
    r=""
    for i in xrange(len(s)/2):
        if s[i*2]==s[i*2+1]:
            return False
        r=r+winp[s[i*2:i*2+2]]
    return red(r)
def check(s,r):
    if len(r)==0:
        return s if red(s) else None
    for i in xrange(len(r)):
        ch=check(s+r[i],r[:i]+r[i+1:])
        if ch:
            return ch
    return None
def solve_bf(case):
    _,R,P,S=case
    return check("","P"*P+"R"*R+"S"*S)


def get_order(d):
    if d==0:
        return "PRS",None
    else:
        o,_=get_order(d-1)
        w=winp[o[0]+o[1]]+winp[o[0]+o[2]]+winp[o[1]+o[2]]
        return w, {w[0]:o[0]+o[1], w[1]:o[0]+o[2], w[2]:o[1]+o[2]}
orders=[get_order(d) for d in range(13)]
def double(s, o):
    _,oe=orders[o]
    r="".join([ oe[c] for c in s ])
    return r
def expand(c, N):
    for o in range(N,0,-1):
        c=double(c,o)
    return c

def cnt(s):
    return (s.count("R"),s.count("P"),s.count("S"))
expansions=[ dict([ (cnt(s),s) for s in [expand(c,n) for c in "RPS"] ]) for n in range(13) ]



def solve(case):
    N,R,P,S=case
    return expansions[N].get((R,P,S),None)





def outcome_string(outcome):
    return "{}".format(outcome) if outcome else "IMPOSSIBLE"


def save_outcomes(path, outcomes):
    with open(path,'w') as f:
        for n,o in enumerate(outcomes):
            f.write("Case #{0}: {1}\n".format( n+1 , outcome_string(o) ))
def process(path_in, path_out=None):
    if path_out==None:
        path_out=path_in.rsplit(".",1)[0]+".out"
    cases=load_cases(path_in)
    outcomes=[solve(c) for c in cases]
    save_outcomes(path_out, outcomes)
    





########## SOLUTIONS TESTING ##########


def verify_outcome(case, outcome):
    return outcome==solve_bf(case)

def test_solutions(path_in, until_first_fail=True):
    cases=load_cases(path_in)
    for cn,c in enumerate(cases):
        o=solve(c)
        if not verify_outcome(c,o):
            print "Wrong outcome!"
            print "Case #{0}:".format(cn)
            print c
            print "Outcome:"
            print o
            if until_first_fail:
                return c
            else:
                print "\n\n"
                
def gen_cases():
    ### IMPLEMENT ###
    return []

def test_solutions_gen(until_first_fail=True):
    cases=gen_cases()
    for cn,c in enumerate(cases):
        o=solve(c)
        if not verify_outcome(c,o):
            print "Wrong outcome!"
            print "Case #{0}:".format(cn)
            print c
            print "Outcome:"
            print o
            if until_first_fail:
                return c
            else:
                print "\n\n"