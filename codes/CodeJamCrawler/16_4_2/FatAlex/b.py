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
    N,K=read_tuple(f)
    Ps=[float(x) for x in read_line(f).split()]
    return K,Ps


def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
            cases.append(load_single_case(f))
    return cases




def max_prob_h(n, e, Ps, h):
    if (n,e) not in h:
        if e>n or e<-n:
            res=0.
        elif n==0:
            res=1.
        else:
            res=Ps[n-1]*max_prob_h(n-1,e-1,Ps,h)+(1.-Ps[n-1])*max_prob_h(n-1,e+1,Ps,h)
        h[(n,e)]=res
    return h[(n,e)]
def loop_sel(Ps, k, Pp):
    if k==0:
        return max_prob_h(len(Ps),0,Ps,{})
    elif len(Pp)==0:
        return 0.
    ps=loop_sel(Ps+[Pp[0]],k-1,Pp[1:])
    pns=loop_sel(Ps,k,Pp[1:])
    return max(ps,pns)
'''def max_prob_h(n, k, e, Ps, h):
    if (n,k,e) not in h:
        if k>n:
            res=0.
        elif e>k or e<-k:
            res=0.
        elif k==0:
            res=1.
        else:
            res=max( max_prob_h(n-1,k,e,Ps,h), Ps[n-1]*max_prob_h(n-1,k-1,e-1,Ps,h)+(1.-Ps[n-1])*max_prob_h(n-1,k-1,e+1,Ps,h)  )
        h[(n,k,e)]=res
    return h[(n,k,e)]'''
'''def max_prob_h(n, k, Ps, h):
    if (n,k) not in h:
        if k>n:
            res={}
        elif k==0:
            res={0:1.}
        else:
            res={}
            ra=max_prob_h(n-1,k-1,Ps,h)
            rr=max_prob_h(n-1,k  ,Ps,h
            for e in xrange(-k,k,2):
                p=max_prob_h()
        h[(n,k,e)]=res
    return h[(n,k)]'''
        


def solve(case):
    K,Ps=case
    res=loop_sel([],K,Ps)
    return res






def outcome_string(outcome):
    return "{:.10f}".format(outcome)


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