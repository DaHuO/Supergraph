def read_list(f):
    return [int(x) for x in f.readline().split()]
def read_tuple(f):
    return tuple(read_list(f))

def load_single_case(f):
    return read_tuple(f)[0]


def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
            cases.append(load_single_case(f))
    return cases




def count(N):
    if not N:
        return None
    x=N
    digits=set()
    while True:
        digits=digits|set(str(x))
        if len(digits)==10:
            return x
        x=x+N

def solve(case):
    N=case
    return count(N)






def outcome_string(outcome):
    return "{}".format(outcome) if outcome else "INSOMNIA"


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
    ### IMPLEMENT ###
    return outcome==solve(case)

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