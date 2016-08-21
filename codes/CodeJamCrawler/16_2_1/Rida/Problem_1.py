num=int(input())
a=[]
output_text= open("outputPPP1.txt","w")


for j in range(num):
    dd=[]
    a = list(input())
    b=len(a)
    for i in range(b):
        if 'Z' in a:
            dd.append('0')
            a.remove('Z')
            a.remove('O')
            a.remove('E')
            a.remove('R')
            b=len(a)
        if 'G' in a:
            dd.append('8')
            a.remove('E')
            a.remove('I')
            a.remove('G')
            a.remove('H')
            a.remove('T')
            b=len(a)
        if 'X' in a:
            dd.append('6')
            a.remove('S')
            a.remove('I')
            a.remove('X')
            b=len(a)
        if 'W' in a:
            dd.append('2')
            a.remove('T')
            a.remove('W')
            a.remove('O')
            b=len(a)
        if 'U' in a:
            dd.append('4')
            a.remove('F')
            a.remove('O')
            a.remove('U')
            a.remove('R')
            b=len(a)
        if 'U' not in a and 'W' not in a and 'X' not in a and 'G' not in a and 'Z' not in a:
            break
    for i in range(b):
        if 'T' in a:
            dd.append('3')
            a.remove('T')
            a.remove('H')
            a.remove('R')
            a.remove('E')
            a.remove('E')
            b=len(a)
        if 'S' in a:
            dd.append('7')
            a.remove('S')
            a.remove('E')
            a.remove('V')
            a.remove('E')
            a.remove('N')
            b=len(a)
        if 'F' in a:
            dd.append('5')
            a.remove('F')
            a.remove('I')
            a.remove('V')
            a.remove('E')
            b=len(a)
        if 'T' not in a and 'F' not in a and 'S' not in a:
            break
        
    for k in range(b):
        if 'O' in a:
            dd.append('1')
            a.remove('O')
            a.remove('N')
            a.remove('E')
            b=len(a)
        if 'O' not in a :
            break
    for p in range(b):
        if 'I' in a:
            dd.append('9')
            a.remove('I')
            a.remove('N')
            a.remove('N')
            a.remove('E')
            b=len(a)

    ss=''.join(dd)
    l=sorted(list(ss))
    oo = ''.join(l)
    #print(oo)
    s= "Case #" +str(j+1)+": "+oo
    output_text.writelines(s)
    output_text.writelines("\n")
output_text.close()
            

