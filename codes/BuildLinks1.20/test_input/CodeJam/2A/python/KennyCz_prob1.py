import sys
from sets import Set
import itertools



def Winner(st1, st2):
    st = Set({st1, st2})
    if st == Set({'P', 'S'}):
        return 'S'
    if st == Set({'S', 'R'}):
        return 'R'
    if st == Set({'R', 'P'}):
        return 'P'

def NextRnd(st):
    ans = []
    for i in range(0,len(st),2):
        if st[i] == st[i+1]:
            return None
        ans.append(Winner(st[i], st[i+1]))
    return ans

def Works(st):
    while len(st) > 1:
        st = NextRnd(st)
        if not st:
            return False
    return True


def answer(query):
    lst1 = ['R'] * query[1] + ['P'] * query[2] + ['S'] * query[3]
    perms = Set(itertools.permutations(lst1))
    #print perms
    anslist = sorted(["".join(item) for item in perms if Works(item)])


    if anslist:
        return anslist[0]
    return 'IMPOSSIBLE'


if __name__ == "__main__":

    T = int(sys.stdin.next())
    queries = []
    for i in range(T):
        queries.append(list(map(int, sys.stdin.next().rstrip().split(' '))))
    for i,st in enumerate(queries):
        print "".join(["Case #", str(i+1), ": ", answer(st)])



