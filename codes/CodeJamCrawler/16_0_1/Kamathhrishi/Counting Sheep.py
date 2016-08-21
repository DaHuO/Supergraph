
def Input():

    fp=open("C:\\Users\\Hrishikesh\\Downloads\\A-large.in","r")
    a=fp.readlines()
    b=[]
    for i in a:

        u=i
        u=u.replace("\n","")
        b.insert(len(b),int(u))

    return b
    
Test=Input()
Input=[]
Output=[]

def Addition(Lis):

    Q=0
    
    if 1 in Lis:
        
        Q+=1
        
    if 2 in Lis:
        
        Q+=1
        
    if 3 in Lis:
        
        Q+=1
        
    if 4 in Lis:
        
        Q+=1

    if 5 in Lis:
        
        Q+=1

    if 6 in Lis:
        
        Q+=1

    if 7 in Lis:
        Q+=1

    if 8 in Lis:
        
        Q+=1

    if 9 in Lis:
        
        Q+=1
        
    if 0 in Lis:
        Q+=1

    if Q==10:

        return True
    
    else:

        return False
    
for i in range(1,len(Test)):
  
    
  L=[]  
  N=Test[i]
  
  Input.insert(len(Input),N)
  
  N=str(N)
  U=N
  i=1
  if N=="0":

      Output.insert(len(Output),N)

  else:
      
      while Addition(L)!=True:
      
        for j in str(N):
            

             L.insert(len(L),int(j))


        if Addition(L)==True:
                             
               Output.insert(len(Output),N)
               break

        else:

             N=int((U))*int((i+1))
             i+=1

for i in range(0,len(Input)):
    q=""
    q+="Case #"
    q+=str(i+1)
    q+=":  "
    if (str(Output[i]))!="0":
        
          q+=str(Output[i])
          
    else:
        
          q+=str("INSOMNIA")
          
    print q

    
  
      

      
  
  

      
      
    
