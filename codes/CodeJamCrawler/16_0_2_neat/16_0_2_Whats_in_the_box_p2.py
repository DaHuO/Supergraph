def solve_N(N):
    mapped = map(lambda x: x == "+", N)
    counter = 0
    while not all(mapped):
        counter = counter + 1
        first = mapped[0]
        for i in range(len(mapped)):
            if first == mapped[i]:
                mapped[i] = not mapped[i]
            else:
                break
    return str(counter)

def solve(Ns):
    for i in range(len(Ns)):
        print "Case #"+str(i+1)+": "+solve_N(Ns[i])

def parse(filename):
    f = open(filename)
    lines = f.readlines()
    num_inputs = int(lines[0])
    inputs = []
    for x in range(num_inputs):
        inputs.append(lines[x+1].strip())
    solve(inputs)

parse("B-large.in")
