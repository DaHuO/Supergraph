# Senate Evacuation
# CodeJam 2016
# Istvan Szabo

alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#f=open("A-test.in")
#f=open("A-small-attempt0.in")
f=open("A-large.in")
input_lines=f.read().splitlines()
f.close

input_lines2=[]
for line in input_lines:
    input_lines2.append([str(s) for s in line.split()])

T=int(input_lines2[0][0])
g = open("output.out", 'w')
for t in range(1,T+1):
    N=int(input_lines2[(t-1)*2+1][0])
    S=list()
    for c in input_lines2[2*t]:
        S.append(int(c))
    g.write('Case #'+str(t)+': ')
    while max(S)!=0:
        maxS=max(S)
        maxvals=[i for i , j in enumerate(S) if j==maxS]
        if sum(S)%2==1 :
            g.write(alphabet[maxvals[0]]+' ')
            S[maxvals[0]]-=1
        elif len(maxvals)==1:
            g.write(alphabet[maxvals[0]]+alphabet[maxvals[0]]+' ')
            S[maxvals[0]]-=2
        else:
            g.write(alphabet[maxvals[0]]+alphabet[maxvals[1]]+' ')
            S[maxvals[0]]-=1
            S[maxvals[1]]-=1
    g.write('\n')
g.close()