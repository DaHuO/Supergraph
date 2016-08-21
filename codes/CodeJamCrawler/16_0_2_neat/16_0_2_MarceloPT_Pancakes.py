import re

def solve(p):
    mov = 0

    mapping = str.maketrans("+-", "-+")
    while True:
        try:
            i = p.rindex("-")
        except:
            return mov
        if i == 0:
            return mov + 1

        if p[0] == "+":
            pl = list(p)
            x = 0
            while p[x] == "+":
                pl[x] = "-"
                x+=1
            mov+=1
            p = ''.join(pl)
        p2 = p[:i+1]
        p2 = p2.translate(mapping)
        p2 = p2[::-1]
        p = p2 + p[i+1:]
        mov+=1

class Pancakes():
    inp = open(r"C:\Users\Marcelo\Documents\Code Jam 2016\Pancakes\B-large.in","r")
    out = open(r"C:\Users\Marcelo\Documents\Code Jam 2016\Pancakes\B-large.out","w")
    lines = inp.readlines()
    i=1
    count=1
    while i<len(lines):
        A = [str(x) for x in re.split(" ",lines[i])]
        """B = [int(x) for x in re.split(" ",lines[i+1])]
        C = [int(x) for x in re.split(" ",lines[i+2])]"""
        out.write("Case #"+str(count)+": "+"{:}".format(solve(''.join(A).rstrip()))+"\n")
        i+=1
        count+=1
    out.close()
    inp.close()