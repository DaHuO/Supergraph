MAX_TIMES = 1000

def shorten(v):
    v = v.rstrip("+")

    while "++" in v:
        v = v.replace("++", "+")
    while "--" in v:
        v = v.replace("--", "-")

    return v

def manu(v, cnt):
    return "".join(["+" if c == "-" else "-" for c in v[:cnt][::-1]]) + v[cnt:]
   
def solve_case(v):
    v = shorten(v)
    if v == "":
        return 0
    if v.startswith("-"):
        v = shorten(manu(v, len(v)))
        return solve_case(v) + 1
    if v.startswith("+"):
        v = shorten(manu(v, len(v) - 1))
        v = shorten(manu(v, len(v)))
        return solve_case(v) + 2
    
    
def solve(fn_in, fn_out):
    f_in = open(fn_in)
    f_out = open(fn_out, "w")
    
    count = int(f_in.readline().strip())

    for i in xrange(1, count+1):
        f_out.write("Case #{}: {}\n".format(i, solve_case( f_in.readline().strip() )))

    f_out.close()

    print open(fn_out).read()

#solve("sample.in.txt", "sample.out.txt")
#solve("B-small-attempt0.in", "B-small-attempt0.out.txt")
solve("B-large.in", "B-large.out.txt")
