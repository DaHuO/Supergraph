from Solve import *

good = "+"
bad = "-"

def pancaceFlip(args):
    
    ps = args[0]
    ps = ps.rstrip(good)
    nFlips = 0
    
    while ps:
        ps = flip(ps)
        ps = ps.rstrip(good)
        nFlips += 1
    return nFlips

def flip(ps):
    rps = ""
    for p in ps:
        if p == good:
            rps += bad
        else:
            rps += good
    return rps

if __name__ == "__main__":
    solveF("B-large.in", pancaceFlip, 1)
