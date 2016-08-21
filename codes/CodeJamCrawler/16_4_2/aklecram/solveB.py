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
            N, K = tuple([int(x) for x in _file.readline().split(" ")])
            probs = tuple([float(x) for x in _file.readline().split(" ")])
            arguments.append((_case + 1, (N, K, probs)))

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

from itertools import combinations

def solve_small(N, K, probs):
    result = 0
    for committee in combinations(range(N), K):
        ptie = 0
        for yes in combinations(committee, K // 2):
            p = 1
            for m in committee:
                p *= probs[m] if m in yes else (1 - probs[m])
            ptie += p
        result = max(result, ptie)
    return "%.8f" % result

def solve(N, K, probs):
    return solve_small(N, K, probs)

run()
#run(Pool(4))
