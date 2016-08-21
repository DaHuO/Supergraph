import sys

fn = sys.argv[1]

with open(fn) as f:
    lines = f.read().splitlines() # removes trailing \n in each line

T = int(lines[0])
output = ""

for i in range(1,T+1):
    output = "Case #%i: " % (i)
    N = int(lines[i])
    if N == 0:
        output += "INSOMNIA"
    else:
        digits = set()
        j = 1
        num = N
        while digits != {0,1,2,3,4,5,6,7,8,9}:
            num = j*N
            nums = str(num)
            for dig in nums:
                digits.add(int(dig))
            j += 1
        output += str(num)
    print(output)
