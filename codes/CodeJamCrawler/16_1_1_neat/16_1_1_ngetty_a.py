

def get_lw(word):
    nw = word[0]
    for c in word[1:]:
        if c < nw[0]:
            nw = nw + c
        else:
            nw = c + nw
    return nw



out = open("alarge.out", 'w')
file = "alarge.in"
count = 1
with open(file, 'r') as infile:
    cases = infile.readlines()[1:]
    for case in cases:
        res = get_lw(case)
        print >> out, "Case #" + str(count) + ": " + res.strip()
        count +=1