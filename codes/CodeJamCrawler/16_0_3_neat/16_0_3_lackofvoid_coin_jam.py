import sys

def get_div(i):
    n = 2
    while n < i**(0.2): # might not find divisors, but is reasonably fast
        if i%n == 0:
            return n
        n += 1
    return -1

fn = sys.argv[1]

with open(fn) as f:
    lines = f.read().splitlines() # removes trailing \n in each line

T = int(lines[0])
assert T == 1
nj = lines[1].split(" ")
N = int(nj[0])
J = int(nj[1])

print("Case #1:")

num_valid = 0
for b in range( int("1"*(N-2), 2)+1 ): # check all possible jamcoins
    formstr = "{:0%ib}" % (N-2)
    jamcoin = "1" + (formstr.format(b)) + "1"
    # print(jamcoin)
    divs = []
    for base in range(2,11):
        # print(int(jamcoin,base))
        divs.append( get_div( int(jamcoin,base) ) )
        if -1 in divs:
            break
    if not (-1 in divs or len(divs) != 9):
        out = jamcoin + " " + " ".join( [ str(d) for d in divs  ] )
        print(out)
        num_valid += 1
        if num_valid >= J:
            break
