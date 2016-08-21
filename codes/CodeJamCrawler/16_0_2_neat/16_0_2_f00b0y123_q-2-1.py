f = open('F:\InteresT\Python\ProblemSet4\Code Jam\cout.txt', 'w')
f.truncate()
powa = open('F:\InteresT\Python\ProblemSet4\Code Jam\B-large.in', 'r+')
w = powa.read()
w = w.split('\n')
for _ in range(int(w[0])):
    n = w[_+1]
    n = list(n)
    i = len(n)-1
    steps = 0
    while i>=0:
        if n[i] == "+":
            i -= 1
        else:
            if n[i] == "-":
                if n[0]=="+":
                    k=0
                    while k<=i:
                        if n[k]!="+":
                            break
                        n[k]="-"
                        k+=1
                else:
                    k=0
                    while k<=i:
                        if n[k]=="-":
                            n[k]="+"
                        else:
                            n[k]="-"
                        k+=1
                    n = n[i::-1] + n[i+1::]
                steps+=1
            counter = 0
            for l in n:
                if l == "+":
                    counter += 1
            if counter == len(n):
                break
    z = "Case #{}: {}".format(_+1, steps)
    f.write(z)
    f.write('\n')
f.close()
powa.close()