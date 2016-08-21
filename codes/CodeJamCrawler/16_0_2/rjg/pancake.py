import sys

f = open(sys.argv[1], 'r')
cases = [line.strip() for line in f]

f.close()
if int(cases[0]) != len(cases) -1:
    print "error"
    sys.exit(1)

def convert(pattern):
    conv = list()
    if len(pattern) == 1:
        return [(pattern, 1)]
    curr_item = pattern[0]
    curr_count = 1
    for item in pattern[1:]:
       if item == curr_item:
           curr_count += 1
       else:
           conv.append((curr_item, curr_count))
           curr_item = item
           curr_count = 1
    conv.append((curr_item, curr_count))
    return conv
    

def pancake(pattern):
    pat = [pat[0] for pat in convert(pattern)]
    if pat[-1] == '+':
        return max(len(pat) - 1, 0)
    if pat[-1] == '-':
        return len(pat)

f = open(sys.argv[1]+'.out', 'w')
for idx, item in enumerate(cases[1:]):
    f.write('Case #%i: %s\n' % (idx+1, pancake(item)))
f.close()
    
