import sys
import itertools

def print_artwork(K, C):
    origins = list(itertools.product(('G', 'L'), repeat=K))
    def next_line(line, origin):
        line1 = []
        for c in line:
            if c == 'G':
                line1.append('G' * len(origin))
            if c == 'L':
                line1.append(origin)
        return ''.join(line1)
    for origin in origins:
        origin = ''.join(origin)
        print "%s:" % origin,
        line = origin
        for i in range(C-1):
            line = next_line(line, origin)
        for i in range(0, len(line), len(origin)):
            print line[i:i+len(origin)],
        print

def find_positions(K, C):
    start = 1
    end = K**C
    for i in range(min(K, C-1)):
        w = (end - start + 1) / K
        # print "w", w
        start += w * i
        end = start + w - 1
        # print start, end
    if K > C-1:
        start += C-1
    else:
        start = end
    return start, end

def main():
    T = int(sys.stdin.readline())
    for t in range(1, T+1):
        K, C, S = map(int, sys.stdin.readline().split())
        # print_artwork(K, C)
        a, b = find_positions(K, C)
        print "Case #%d:" % t, 
        if b - a + 1 > S:
            print "IMPOSSIBLE"
        else:
            print " ".join(map(str, range(a, b+1)))

if __name__ == "__main__":
    main()
