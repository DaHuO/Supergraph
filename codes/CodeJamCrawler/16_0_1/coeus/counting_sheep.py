import fileinput

def solve(n):
    if n == 0: return "INSOMNIA"
    is_found = [False] * 10

    composite = n
    while not(all(is_found)):
        for c in str(composite):
            c_int = int(c)
            is_found[c_int] = True
        
        if all(is_found): 
            return str(composite)
        else:
            composite += n


do_see_first = False
case = 1
for ln in fileinput.input():
    if not do_see_first:
        do_see_first = True
        continue
    
    print "Case #%s: %s" % (case, solve(int(ln.strip())))
    case += 1
