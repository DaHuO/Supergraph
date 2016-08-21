import sys
from collections import Counter

rules = [('ZERO', 'Z', 0),
         ('TWO', 'W', 2),
         ('FOUR', 'U', 4),
         ('SIX', 'X', 6),
         ('EIGHT', 'G', 8),
         ('ONE', 'O', 1),
         ('THREE', 'T', 3),
         ('FIVE', 'F', 5),
         ('SEVEN', 'S', 7),
         ('NINE', 'I', 9)]

def remove_chars(counts, dig, n):
    if n == 0: return
    for c in dig:
        counts[c] -= n

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as fp:
        n_cases = int(fp.readline().strip())

        for i, line in enumerate(fp.readlines()):
            counts = Counter(list(line.strip()))

            res = [0 for ii in range(10)]

            for rule in rules:
                res[rule[2]] = counts[rule[1]]
                remove_chars(counts, rule[0], res[rule[2]])

            for k in counts:
                if counts[k] != 0:
                    sys.stderr.write("ERROR")
                    print counts
                    exit()
            
            ph = ""
            for j, n in enumerate(res):
                ph = ph + str(j)*n
                
            print "Case #{0}: {1}".format(i+1, ph)
            

            
