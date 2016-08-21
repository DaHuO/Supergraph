def insomnia(n,f):
    if n == 0:
        f.write("INSOMNIA\n")       
    else:
        d = {}
        counter = 0
        while len(d.keys())< 10:
            counter += n
            workspace = counter
            while workspace > 0:
                if(workspace%10) not in d.keys():
                    d[(workspace%10)] = ""
                workspace = workspace/10
        f.write(str(counter)+"\n")
                


f = open('A-large.in')
lines = f.readlines()
x = int(lines[0].strip())
f = open('result.txt', 'a')
for r in range(1,x+1,1):
    
    f.write ("Case #" + str(r) + ": ")
    insomnia (int(lines[r].strip()),f)
f.close()
