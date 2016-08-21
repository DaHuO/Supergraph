with open("A-large.in") as infile:
    lines = [a.strip() for a in infile.readlines()[1:]]
   
out = []   
x = 1    
for n in lines:
    mm = 10**int(n) +1
    num = int(n)
    sf = set(n)
    i = 2
    num2 = num
    while len(sf) < 10 and i <= mm:
        num2 *= i
        n = str(num2)
        for l in n:
            sf.add(l)
        i += 1
        num2 = num
    if i <= mm:
        out.append("Case #{}: {}\n".format(x, num*(i-1)))
    else:
        out.append("Case #{}: INSOMNIA\n".format(x))
    x += 1
        
with open("out", "w") as outfile:
    outfile.writelines(out)
