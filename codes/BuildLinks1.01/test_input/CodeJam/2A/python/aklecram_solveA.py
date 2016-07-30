import sys
from multiprocessing import Pool

# Add git repository with helpers to path
# The repo is publicly available at git@github.com:marcelka/cocoli.git
sys.path.append("/home/marcelka/projects/cocoli/")

def run(pool=None): # {{{
    inp=sys.argv[1]
    outp="%s.out" % inp.split(".")[0]

    with open(inp, 'r') as _file, open(outp, 'w') as out:
        _cases = int(_file.readline())
        arguments = []
        for _case in range(_cases):
            N, R, P, S = tuple([int(x) for x in _file.readline().split(" ")])
            arguments.append((_case + 1, (N, R, P, S)))

        if pool == None:
            results = list(map(solve_wrapper, arguments))
        else:
            results = sorted(
                list(pool.imap_unordered(solve_wrapper, arguments)),
                key=lambda r: r[0])
        assert(len(results) == _cases)
        
        for _case, result in results:
            out.write("Case #%s: %s\n" % (_case, result))

def solve_wrapper(args):
    case_no, _args = args
    print("Solving case #%s" %(case_no))
    return (case_no, solve(*_args))
# }}}

def lineup(N, top):
    if N == 0: return top
    prev = {
      "P": "PR",
      "R": "RS",
      "S": "PS",
    }[top]
    return lineup(N - 1, prev[0]) + lineup(N - 1, prev[1])

def order(ln):
    l = len(ln) // 2
    if l == 0:
        return ln
    else:
        a = order(ln[:l])
        b = order(ln[l:])
        if a < b: return a + b
        else: return b + a

def count_ok(P, R, S, ln):
    if ln.count("P") != P: return False
    if ln.count("R") != R: return False
    if ln.count("S") != S: return False
    return True

def solve(N, R, P, S):
    pl = order(lineup(N, "P"))
    rl = order(lineup(N, "R"))
    sl = order(lineup(N, "S"))
    for l in sorted([pl, rl, sl]):
        if count_ok(P, R, S, l): return l
    return "IMPOSSIBLE"

run()
#run(Pool(4))
