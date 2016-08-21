
def rev(char):
    if char == '+':
        return '-'
    return '+'


def flip(seq, end):
    s = list(seq)
    i = 0
    j = end
    while i <= j:
        i_new = rev(s[j])
        j_new = rev(s[i])
        s[i] = i_new
        s[j] = j_new
        i += 1
        j -= 1
    return ''.join(s)


def solve(seq):

    end = len(seq) - 1
    while seq[end] == '+' and end >= 0:
        end -= 1
    if end < 0:
        return 0

    visited = set()
    start = seq[0:end+1]
    bfs = [(start, 0)]
    visited.add(start)
    win = ''.join(['+' for _ in xrange(end+1)])

    while len(bfs) > 0:
        curr, d = bfs.pop(0)
        for i in xrange(len(curr)):
            currx = flip(curr, i)
            if currx not in visited:
                bfs.append((currx, d+1))
                visited.add(currx)
            if currx == win:
                return d+1

    return -1

if __name__ == '__main__':
    input = 'B-small-attempt0.in'
    output = 'B-small-attempt0.out'

    with open(input) as f:
        content = f.readlines()
    content = [x.strip('\n') for x in content]

    with open(output, 'w') as o:
        for i, p in enumerate(content[1:]):
            o.write('Case #%d: %d' % ((i+1), solve(p)))
            o.write('\n')
