TEST="""5
1 1 1 0
1 2 0 0
2 1 1 2
2 2 0 2
12 2 3 3
"""
#raw_input = iter(TEST.splitlines()).next

def solve(n,r,p,s):
    #winner determines entire lineup, but not positions.
    l = []
    for poss_winner in ["R", "S", "P"]:
        poss_answer = round_with_winner(n, poss_winner)
        l.append(poss_answer)
    new_l = filter(lambda x: comp_count_correct(x,r,p,s), l)
    new_l.sort()
    if new_l:
        return new_l[0]
    else:
        return "IMPOSSIBLE"
    

def comp_count_correct(ans,r,p,s):
    correct = (ans.count("R") == r) and (ans.count("P") == p) and (ans.count("S") ==s)
    return correct

def round_with_winner(n, winner):
    if n == 1:
        if winner == "R":
            return "RS"
        elif winner == "S":
            return "PS"
        elif winner == "P":
            return "PR"

    else:
        if winner == "R":
            a =  round_with_winner(n-1, "R")
            b =  round_with_winner(n-1, "S")
        elif winner == "S":
            a =  round_with_winner(n-1, "P")
            b =  round_with_winner(n-1, "S")
        elif winner == "P":
            a =  round_with_winner(n-1, "P")
            b =  round_with_winner(n-1, "R")
    l = [a,b]
    l.sort()
    return "".join(l)

if __name__=="__main__":
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n,r,p,s = [int(s) for s in raw_input().split(" ")]
        print "Case #{}: {}".format(i, solve(n,r,p,s))
          # check out .format's specification for more formatting options
