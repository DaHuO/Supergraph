import fileinput

# this only works for the small dataset where K=S
# by checking the first K tiles, we either hit all gold because the first
# element was G, or a 1:1 copy of the original pattern if the first element was L
# in any case, it should always be possible and we have a trivial answer.
def get_solution(line):
    [K, C, S] = [int(e) for e in line.split(' ')]
    if K > S:
        return "IMPOSSIBLE"
    return " ".join([str(x) for x in range(1,K+1)])

for (linenr, line) in enumerate(fileinput.input()):
    line = line[:-1]
    if fileinput.isfirstline():
        n = int(line)
        continue
    if linenr>n:
        print 'too few lines'
        break

    print 'Case #%d: %s' % (linenr, get_solution(line))

    
    
    
