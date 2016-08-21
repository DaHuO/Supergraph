import sys
sys.setrecursionlimit(10000)
fobj_in = open("B-large.in")
fobj_out = open("output.txt","w")
i = 1
listt=[0]
flips=0
def check():
   
    if listt[0]=='+':
            checkp(0)
    elif listt[0]=='-':
            checkm(0)
    
    
def checkp(s):
    global listt,flips

    try:
        if listt[s]=='+':
          
            checkp(s+1)
        elif listt[s]=='-':
            rev=listt[0:s]
            rev.reverse()
            temp=[]
            for r in rev:
                if r=='+':
                    temp.append('-')
                else:
                    temp.append('+')
            listt=temp+listt[s:]
            flips+=1
            check()

    except IndexError:
       
        pass

def checkm(s):
 
    global listt,flips
    try:
        if listt[s]=='+':
            rev=listt[0:s]
            rev.reverse()
            temp=[]
            for r in rev:
                if r=='+':
                    temp.append('-')
                elif r=='-':
                    temp.append('+')
            listt=temp+listt[s:]
            flips+=1
         
            check()
        elif listt[s]=='-':
                checkm(s+1)
        else:
            rev=listt[0:s]
            rev.reverse()
            temp=[]
            for r in rev:
                if r=='+':
                    temp.append('-')
                elif r=='-':
                    temp.append('+')
         
            listt=temp+listt[s+1:]
            flips+=1
    except IndexError:
        rev=listt[0:s]
        rev.reverse()
        temp=[]
        for r in rev:
            if r=='+':
                temp.append('-')
            elif r=='-':
                temp.append('+')
       
        listt=temp+listt[s:]
        flips+=1
        
for line in fobj_in:
    cases=0
    flips=0
    if i>1:
     
        length=len(line)
        listt=list(line)
        check()
        fobj_out.write("Case #"+str(i-1) + ": " + str(flips)+'\n')
    elif i==1:
       
        cases=int(line)
    i = i + 1
   
    if i==cases+2:
        break
fobj_in.close()
fobj_out.close()
