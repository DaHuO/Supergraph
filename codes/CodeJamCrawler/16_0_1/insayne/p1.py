def read_file():
    for line in open("A-large.in","r"):
        yield line.strip()

cin = read_file().next

def write_line(line):
    open("output.txt","a").write(str(line) + "\n")

cout = write_line


t = int(cin())

o = set("0123456789")
for _t in range(t):
    n = int(cin())
    s = set(str(n))
    if n == 0:
        a = "Case #" + str(_t+1) + ": INSOMNIA"
        cout(a) 
    else:
        i = 2
        while True:
           
            a = set(str(n*i))
            s.update(a)
            
            if o == s:
                a= "Case #" + str(_t+1) + ":" + " " + str(n*i)
                cout(a)
                break
            i+=1
    
