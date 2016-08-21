import fileinput

out_file = open('outputA_large', 'w');

def solve(n):
    if(int(n) == 0):
        return "INSOMNIA"
    i = 1
    digits = set()
    n = int(n)
    while(len(digits) != 10):
         c = str(i*n)
         digits = digits.union(set(c))
         i+=1
    return c

for i,line in enumerate(fileinput.input("A-large.in")):
    if i != 0:
        n = line.strip()
        ans = "Case #%i: "%i + solve(n)
        out_file.write(ans + '\n');

out_file.close()