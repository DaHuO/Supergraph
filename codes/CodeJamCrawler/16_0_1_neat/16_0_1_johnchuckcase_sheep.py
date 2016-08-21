def find_last_number(n):
    seen = set(str(n))
    multiplier = 2
    new_n = n

    if multiplier * new_n == new_n:
        return 'INSOMNIA'

    while len(seen) < 10:
        new_n = n * multiplier
        seen.update(str(new_n))
        multiplier += 1
    return new_n

def wrapper(f):

    with open('/Users/johncase/Desktop/output.txt','w') as out:
        f.readline()

        for case, n in enumerate(f):
            # print case, int(n)
            out.write("Case #" + str(case + 1) + ": " + str(find_last_number(int(n))) + '\n')

wrapper(open('/Users/johncase/Downloads/A-large.in','r'))
# wrapper(open('/Users/johncase/Documents/projects/codejam/sheep_file.txt','r'))
