def read_file():
    for line in open("B-large.in","r"):
        yield line.strip()

cin = read_file().next

def write_line(line):
    open("output.txt","a").write(str(line) + "\n")

cout = write_line

t = int(cin())

for _t in range(t):
    s = cin()
    pl = s[0]
    c = 0
    for i in range(len(s)):
        if s[i] != pl:
            s = s[i] * i + s[i:]
            c += 1
            pl = s[i]
    if s[0] == "-":
        c+=1

    a= "Case #" + str(_t+1) + ":" + " " + str(c)
    cout(a)
