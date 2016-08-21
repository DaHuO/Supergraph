
def num_flips(pc):
    cur = 0
    while pc.endswith("+"):
        pc = pc[:-1]
    while len(pc) != 0:
        if pc.endswith("-"):
            while pc.endswith("-"):
                pc = pc[:-1]
            cur += 1
        elif pc.endswith("+"):
            while pc.endswith("+"):
                pc = pc[:-1]
            cur += 1
    return cur


x = int(raw_input())
pancakes = []
for i in range(0, x):
    pancakes.append(raw_input())

for j in range(0, len(pancakes)):
    print "Case #" + str(j+1) + ": " + str(num_flips(pancakes[j]))


