def count(num):
    res = set()
    for c in str(num):
        res.add(c)
    return res

def solve(n):
    if n == 0:
        return "INSOMNIA"
    else:
        digits = set()
        i = 1
        while len(digits) < 10:
            digits |= count(i*n)
            i += 1
        return (i-1)*n

filename = input("Enter filename: ")
file = open(filename, 'r')

outfile = open(filename.replace('in','out'), 'w')

t = int(file.readline().strip())
for i in range(t):
    n = int(file.readline().strip())
    outfile.write("Case #{}: {}\n".format(i+1, solve(n)))
    
file.close()
outfile.close()