# Revenge of the pancakes
# CodeJam 2016
# Istvan Szabo



#f=open("B-small-attempt1.in")
#f=open("B-test.in")
f=open("B-large.in")
input_lines=f.read().splitlines()
f.close

input_lines2=[]
for line in input_lines:
    input_lines2.append([str(s) for s in line.split()])

T=int(input_lines2[0][0])
g = open("output.out", 'w')

for i in range(T):
    print(i)
    pancakes=[]
    for s in input_lines2[i+1][0]:
        pancakes.append(s)
    R=0
    if pancakes==['-']:
        g.write('Case #'+str(i+1)+': '+str(1)+'\n')
    elif pancakes==['+']:
        g.write('Case #'+str(i+1)+': '+str(0)+'\n')
    else:
        for j in range(1,len(pancakes)):
            if pancakes[j]!=pancakes[j-1]: R=R+1
        if pancakes[len(pancakes)-1]=='-': R=R+1
        g.write('Case #'+str(i+1)+': '+str(R)+'\n')
g.close()
