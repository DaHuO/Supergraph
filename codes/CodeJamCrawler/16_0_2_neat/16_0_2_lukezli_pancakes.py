f = open("B-large.in", "r")
num_lines = int(f.readline())

CORRECT = 1
WRONG = 0

def calc(pancakes):
    if len(pancakes) == 0: return 0
    if pancakes[-1] == CORRECT:
        return calc(pancakes[:-1])
    else:
        extra_cost = 2 if pancakes[0] == CORRECT else 1

        j = 0
        while(pancakes[j] == CORRECT):
            pancakes[j] = WRONG
            j += 1
        
        new_cakes = pancakes[::-1][:-1]
        return extra_cost + calc([1 - a for a in new_cakes])

for i in range(num_lines):
    pancakes = [CORRECT if p == "+" else WRONG for p in list(f.readline().strip())]
    
    print "Case #" + str(i+1) + ":", calc(pancakes)
