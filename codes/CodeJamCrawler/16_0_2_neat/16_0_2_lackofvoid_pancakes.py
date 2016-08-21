import sys

fn = sys.argv[1]

with open(fn) as f:
    lines = f.read().splitlines() # removes trailing \n in each line

T = int(lines[0])
output = ""

for i in range(1,T+1):
    S = lines[i]
    num_moves = 0
    while S != "+"*len(S):
        j = 0
        while j < len(S) and S[j] == S[0]:
            j += 1
        flipped = "+" if S[0] == "-" else "-"
        S = flipped*(j-1) + S[j:]
        num_moves += 1
    print("Case #%i: %i" % (i, num_moves))
