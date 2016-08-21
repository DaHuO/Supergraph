from sets import Set

def solve_N(N):
    if N == 0:
        return "INSOMNIA"
    digits = Set([])
    i = 0
    while len(digits) < 10:
        i = i + 1
        digits = digits.union(Set(str(N*i)))
    return str(N*i)

def solve(Ns):
    for i in range(len(Ns)):
        print "Case #"+str(i+1)+": "+solve_N(Ns[i])

def parse(filename):
    f = open(filename)
    lines = f.readlines()
    num_inputs = int(lines[0])
    inputs = []
    for x in range(num_inputs):
        inputs.append(int(lines[x+1]))
    solve(inputs)
    

parse("A-large.in")
