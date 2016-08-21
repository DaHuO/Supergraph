'''run in same directory as input file'''
import sys
from os.path import splitext
import string

infile_name = sys.argv[1]
infile = open(infile_name)
outfile = open('solve_{}.txt'.format(splitext(infile_name)[0]), 'w')


def write_solution(case_nr, solution):
    outfile.write('Case #{}: {}\n'.format(case_nr, solution))

count = int(infile.readline())

for case_nr, case in enumerate(range(count), 1):
    n = int(infile.readline())
    counts = (
        (int(count), string.ascii_uppercase[i])
        for i, count in enumerate(infile.readline().split())
    )
    at_leasts = {}
    for count, letter in counts:
        for j in xrange(count):
            at_leasts.setdefault(j+1, []).append(letter)

    # start evacuation
    evacuations = []
    maxcount = max(at_leasts.iterkeys())
    for count in xrange(maxcount, 0, -1):
        senators = at_leasts.get(count, [])

        def evacuate_senators():
            if len(senators) in (1, 3):
                evacuations.append(senators.pop())
            else:
                evacuations.append(senators.pop() + senators.pop())

        while senators:
            evacuate_senators()

    write_solution(case_nr, ' '.join(evacuations))
