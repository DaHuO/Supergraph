import sys

def count(n):
    if n == 0:
        return 'INSOMNIA'
    else:
        x = set(str(n))
        multiplier = 1
        while (len(x)<10)and(multiplier<1e+8):
            updated_number = multiplier*n
            x = x.union(str(updated_number))
            multiplier += 1
        return str(updated_number) if len(x)==10 else 'INSOMNIA'

problem_input = sys.stdin.readlines()
the_T = int(problem_input[0])
assert the_T == len(problem_input[1:])

for i,the_N in enumerate(problem_input[1:]):
    the_N = int(the_N)
    print "Case #%d: %s"%(i+1,count(the_N))