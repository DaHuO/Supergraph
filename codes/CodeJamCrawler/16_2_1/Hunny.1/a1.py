"""
    Author : NILESH AGARWAL
    Gmail : nilesh.kumpawat@gmail.com
"""
def mobile_number(l):
    l = list(l)
    m = []
    while True:
        if "Z" in l:
            l.remove("Z")
            l.remove("E")
            l.remove("R")
            l.remove("O")
            m.append("0")
        else:
            break
    while True:
        if "W" in l:
            l.remove("T")
            l.remove("W")
            l.remove("O")
            m.append("2")
        else:
            break
    while True:
        if "U" in l:
            l.remove("F")
            l.remove("O")
            l.remove("U")
            l.remove("R")
            m.append("4")
        else:
            break
    while True:
        if "X" in l:
            l.remove("S")
            l.remove("I")
            l.remove("X")
            m.append("6")
        else:
            break
    while True:
        if "G" in l:
            l.remove("E")
            l.remove("I")
            l.remove("G")
            l.remove("H")
            l.remove("T")
            m.append("8")
        else:
            break
    while True:
        if "O" in l:
            l.remove("O")
            l.remove("N")
            l.remove("E")
            m.append("1")
        else:
            break
    while True:
        if "S" in l:
            l.remove("S")
            l.remove("E")
            l.remove("V")
            l.remove("E")
            l.remove("N")
            m.append("7")
        else:
            break
    while True:
        if "F" in l:
            l.remove("F")
            l.remove("I")
            l.remove("V")
            l.remove("E")
            m.append("5")
        else:
            break
    while True:
        if "I" in l:
            l.remove("N")
            l.remove("I")
            l.remove("N")
            l.remove("E")
            m.append("9")
        else:
            break
    while True:
        if "H" in l:
            l.remove("T")
            l.remove("H")
            l.remove("R")
            l.remove("E")
            l.remove("E")
            m.append("3")
        else:
            break
    m = sorted(m)
    return "".join(m)
            
cases=0
filer = open('ia2.in')
filew = open('poa2.txt','w')
matrix = filer.read()
matrix = [item.split() for item in matrix.split('\n')[:-1]]
cnt = 0
t = int(matrix[cnt][0])
cnt=cnt+1
for q in range(t):
    l = matrix[cnt][0]
    cnt=cnt+1
    cases = cases+1
    filew.write("Case #"+str(cases)+":"+" ")
    string = mobile_number(l)
    filew.write(string+" \n")
filew.close()
filer.close()
