import argparse

parser = argparse.ArgumentParser()
parser.add_argument('inputs',type=argparse.FileType('r'))
parser.add_argument('output',type=argparse.FileType('w'))
args = parser.parse_args()

def swapsgn(sign):
    if sign == '+':
        return '-'
    else:
        return '+'

def rotate(l,lastid):
    if len(l) == 1:
        l[0] = swapsgn(l[0])
    else:
        for i in xrange(lastid,0,-1):
            l[i-1] = swapsgn(l[i-1])

case = 0
next(args.inputs)
for inp in args.inputs:
    inp = list(inp.rstrip('\n'))
    count = 0
    count = 0
    while not all('+' == v for v in inp):
        lastid = len(inp) - inp[::-1].index('-')
        rotate(inp,lastid)
        count += 1
    case += 1
    args.output.write(("Case #%i: %s\n")%(case,count))
