
#============================================

curProblem = "A";
curAttempt = 0;
curType = "example";
#curType = "practice";
#curType = "small";
curType = "large";

exampleString = """
7
CAB
JAM
CODE
ABAAB
CABCBBABC
ABCABCABC
ZXCASDQWE
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
    outBuf = buf;
    return outBuf;

def solveProblem(rnd, x):
    ## Do actions

    db = set( "%s"%(x[0]) );
    for _,v in enumerate(x[1:]):
        ndb=set();
        for e in db:
            ndb.add("%s%s"%(v,e));
            ndb.add("%s%s"%(e,v));
        db = ndb;

        pairs = { (st[0],st[-1]) for st in db };

        ndb = set();
        for p in pairs:
            ndb.add( max(st for st in db if st[0] == p[0] and st[-1] == p[1]) );
        db = ndb;

    return max(db);

#============================================

from time import time;

if __name__ == '__main__':
    inputData = parseInput(getInput());
    outfile = "%s.out"%(curProblem);

    start=time();
    with open(outfile,"wt") as f:
        for rnd, inp in enumerate(inputData):
            res = solveProblem(rnd, inp);
            st="Case #%d: %s\n"%(rnd+1,res);
            print st[:-1]; f.write(st);

    print "Total time: %fs"%(time()-start);

#============================================
