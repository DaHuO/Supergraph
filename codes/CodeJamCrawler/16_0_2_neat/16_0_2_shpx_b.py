import Queue

name = "B-small-attempt1"
def change(x):
    if x == '-':
        return '+'
    return '-'

def flip(pancakes, i):
    return pancakes[:i] + ''.join([change(x) for x in pancakes[i:]][::-1])


with open(name+'.in', 'r') as f:
    f.readline()
    for case_num, line in enumerate(f):
        pancakes = line.strip()[::-1]
        flips = [(0, pancakes)]
        seen_flips = set(pancakes)
        while True:
            depth, current_flip = flips.pop(0)
            seen_flips.add(current_flip)
            if current_flip.count('-') == 0:
                print "Case #{}: {}".format(case_num+1, depth)
                break
            for y in range(len(current_flip)):
                new_flip = flip(current_flip, y)
                if new_flip not in seen_flips:
                    flips.append((depth+1, new_flip))








