
def solve_case(pancakes):
    """ :type pancakes: str """
    pancakes += '+'

    last_p = pancakes[0]
    flip_count = 0

    for p in pancakes[1:]:
        if p != last_p:
            flip_count += 1
        last_p = p

    return str(flip_count)

# start
f_name = 'B-large'
infile = open(f_name+'.in', 'r')
outfile = open(f_name+'.out', 'w')

T = int(infile.readline().strip())

for ti in range(T):
    pancakes = infile.readline().strip()

    soln = solve_case(pancakes)

    outfile.write('Case #'+str(ti+1)+': '+soln+'\n')

infile.close()
outfile.close()

