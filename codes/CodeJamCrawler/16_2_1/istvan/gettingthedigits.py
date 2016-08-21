# The Last Word
# CodeJam 2016
# Istvan Szabo



#f=open("A-small-practice.in")
#f=open("A-small-attempt1.in")
f=open("A-large.in")
input_lines=f.read().splitlines()
f.close

input_lines2=[]
for line in input_lines:
    input_lines2.append([str(s) for s in line.split()])

T=int(input_lines2[0][0])
g = open("output.out", 'w')
for t in range(1,T+1):
    s=input_lines2[t]
    s_list=[c for c in s[0]]
    result=[0,0,0,0,0,0,0,0,0,0]
    while 'W' in s_list:
        s_list.remove('W')
        s_list.remove('T')
        s_list.remove('O')
        result[2]+=1
    while 'X' in s_list:
        s_list.remove('S')
        s_list.remove('I')
        s_list.remove('X')
        result[6]+=1
    while 'U' in s_list:
        s_list.remove('F')
        s_list.remove('O')
        s_list.remove('U')
        s_list.remove('R')
        result[4]+=1
    while 'F' in s_list:
        s_list.remove('F')
        s_list.remove('I')
        s_list.remove('V')
        s_list.remove('E')
        result[5]+=1
    while 'G' in s_list:
        s_list.remove('E')
        s_list.remove('I')
        s_list.remove('G')
        s_list.remove('H')
        s_list.remove('T')
        result[8]+=1
    while 'V' in s_list:
        s_list.remove('S')
        s_list.remove('E')
        s_list.remove('V')
        s_list.remove('E')
        s_list.remove('N')
        result[7]+=1
    while 'X' in s_list:
        s_list.remove('S')
        s_list.remove('I')
        s_list.remove('X')
        result[6]+=1
    while 'I' in s_list:
        s_list.remove('N')
        s_list.remove('I')
        s_list.remove('N')
        s_list.remove('E')
        result[9]+=1
    while 'N' in s_list:
        s_list.remove('O')
        s_list.remove('N')
        s_list.remove('E')
        result[1]+=1
    while 'O' in s_list:
        s_list.remove('Z')
        s_list.remove('E')
        s_list.remove('R')
        s_list.remove('O')
        result[0]+=1
    while 'R' in s_list:
        s_list.remove('T')
        s_list.remove('H')
        s_list.remove('R')
        s_list.remove('E')
        s_list.remove('E')
        result[3]+=1
    r=''
    for l in range(10):
        for k in range(result[l]):
            r=r+str(l)
    g.write('Case #'+str(t)+': '+ r +'\n')
g.close()
