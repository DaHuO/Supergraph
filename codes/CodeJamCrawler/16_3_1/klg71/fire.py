Partynumber=2
Senators=[3,2,2]
Evacuated=[0,0,0]

def evacuate(Senators,Partynumber,Evacuated):
    if sum(Senators)>0:
        new_senators=list(Senators)
        pos=get_next(Senators,Evacuated)
        new_senators[pos]-=1
        new_evac=list(Evacuated)
        new_evac[pos]+=1
        pos1=""
        if sum(Senators)!=3:
            pos1=get_next(new_senators,Evacuated)
            new_senators[pos1]-=1
            new_evac[pos1]+=1
        return [(pos,pos1)]+evacuate(new_senators,Partynumber,new_evac)
    return []

def get_next(Senators,Evacuated):
    Max=0
    pos=0
    i=0
    for Senator in Senators:
        if Senator>Max:
            Max=Senator
            pos=i
        i=i+1
    return pos
def do_case(Senators,Partynumber,Evacuated,i):
    Result=evacuate(Senators,Partynumber,Evacuated)
    String="Case #"+str(i)+": "
    for step in Result:
        String+=str(chr(step[0]+65))
        if step[1]!="":
            String+=str(chr(step[1]+65))
        String+=" "

    print(String)

politic=[]
number=int(raw_input("Enter TestCases"))
for i in range(0,number):
    parties=int(raw_input("Enter Parties: "))
    politics=list(raw_input("").split(" "))
    politics=[int(x) for x in politics]
    politic.append(politics)

i=1
for politics in politic:
    Evacuated=[0]*len(politics)
    do_case(politics,Partynumber,Evacuated,i)
    i+=1
