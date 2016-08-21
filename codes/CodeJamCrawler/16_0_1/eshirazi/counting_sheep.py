MAX_TIMES = 1000
   
def solve_for_number(n):
    if n == 0:
        return "INSOMNIA"
    
    seen_digits = set()
    for i in xrange(n, n * MAX_TIMES, n):
        seen_digits |= set(str(i))
        if len(seen_digits) == 10:
            return str(i)
    return "INSOMNIA"

def solve(fn_in, fn_out):
    f_in = open(fn_in)
    f_out = open(fn_out, "w")
    
    count = int(f_in.readline().strip())

    for i in xrange(1, count+1):
        f_out.write("Case #{}: {}\n".format(i, solve_for_number( int(f_in.readline().strip()) )))

#solve("sample.in.txt", "sample.out.txt")
#solve("A-small-attempt0.in", "A-small-attempt0.out.txt")
solve("A-large.in", "A-large.out.txt")
