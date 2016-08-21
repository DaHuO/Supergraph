
#============================================

curProblem = "B";
curAttempt = 4;
curType = "example";
#curType = "practice";
curType = "small";
#curType = "large";

exampleString = """
1
2
6 8
2 4
4 8
""";

def getInput():
    if curType == "example": return exampleString;

    fileName = "%s-"%(curProblem);
    if curType == "large": fileName = "%s-large.in"%(curProblem);
    if curType == "small": fileName = "%s-small-attempt%d.in"%(curProblem,curAttempt);
    if curType == "practice": fileName = "%s-small-practice.in"%(curProblem);

    with open(fileName, "rt") as f:
        buf = f.readlines();

    return "".join(buf);

def parseInput(buf):
    buf = buf.split("\n");
    buf = filter(len,buf);

    t = int(buf[0]); buf=buf[1:];
    outBuf = [];
    for _ in xrange(1,t+1):
        n, = parse(buf[0],"i"); buf=buf[1:];
        w = [parse(buf[i],"i"*n) for i in xrange(2*n-1)]; buf=buf[len(w):];

        outBuf.append([n,w]);
        pass;
    return outBuf;

def rec(rem,grid,possible):
    if rem == 0: yield grid;

    for index,cur in enumerate(possible):
        nGrid = grid + [cur];
        nPossible = possible[:index]+possible[index+1:];
        if len(grid) == 0:
            for ret in rec(rem-1,nGrid,nPossible): yield ret;
            continue;

        prev = grid[-1];
        bad=False;
        for c in xrange(len(cur)):
            if prev[c] >= cur[c]: bad=True; break;

        if bad: continue;

        for ret in rec(rem-1,nGrid,nPossible): yield ret;

    return;

def solveProblem(rnd, (n,x)):
    ## Do actions

    x = sorted(x);
    x = map(tuple,x);

    for v in x: print "\t**%s"%(v,);
    
    origSet = set(x);

    origCount = { v : 0 for v in x };
    for v in x: origCount[v]+=1;

    for grid in rec(n,[],x):
        count = { v : origCount[v] for v in x };
    
        for v in grid: print "\t%s"%(list(v));

        rows = [ v for v in grid ];
        cols = [ tuple( grid[r][c] for r in xrange(n) ) for c in xrange(n) ];

        found = set(rows);
        found |= set(cols);

        for v in rows:
            if v not in origSet: count[v]=0;
            count[v]-=1;
#            if count[v] < 0:
#                badNegatives += 1;
#                print "\tdouble count of %s"%(v,);

        for v in cols:
            if tuple(v) not in origSet: count[v]=0;
            count[v]-=1;
#            if count[v] < 0:
#                badNegatives += 1;
#                print "\tdouble count of %s"%(v,);

        bad = False;
        for v in origSet:
            if v not in found:
                print "\tNever scanned %s"%(v,);
                bad = True;

        if bad: continue;
        for v in rows: print "\t\trow %s\t%s"%(v,origCount[v] if v in origSet else -123);
        for v in cols: print "\t\tcol %s\t%s"%(v,origCount[v] if v in origSet else -123);
        for v,ct in count.items(): print "\t\t** %s\t%s"%(v,count[v]);

        ret = 0;
        for v,ct in count.items():
            if ct != 0: return v;

    print "BAD";
    exit(0);
    return [];

#============================================

from argparser import parse, parse1;
from time import time;

if __name__ == '__main__':
    inputData = parseInput(getInput());
    outfile = "%s.out"%(curProblem);

    start=time();
    with open(outfile,"wt") as f:
        for rnd, inp in enumerate(inputData):
            res = solveProblem(rnd, inp);
            res = " ".join(map(str,res));
            st="Case #%d: %s\n"%(rnd+1,res);
            print st[:-1]; f.write(st);

    print "Total time: %fs"%(time()-start);

#============================================
