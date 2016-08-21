#f='2016-stage1B-A-example'
#f='2016-stage1B-A-small-attempt2'
f='2016-stage1B-A-large'
#f='2016D-small'
#f='2016-stage1B-A-small'

dado=['Z','W','G','X','H','S','V','U','O','I']
par=['ZERO','TWO','EIGHT','SIX','THREE','SEVEN','FIVE','FOUR','ONE','NINE']      
in_file = open(f+'.in','r')
out_file = open(f+'.out','w')
num = int(in_file.readline())
print(num)
for i in range(0,num):
    temp = in_file.readline()[:-1]
    print(temp)
    cont=[]
    resultado=[0]*10
    for j in dado:
        cont.append(temp.count(j))        
    print(cont)
    resultado[0]=cont[0]
    resultado[2]=cont[1]
    resultado[8]=cont[2]
    resultado[6]=cont[3]
    resultado[4]=cont[7]

    resultado[7]=cont[5]-resultado[6]
    resultado[3]=cont[4]-resultado[8]
    resultado[5]=cont[6]-resultado[7]
    resultado[1]=cont[8]-resultado[0]-resultado[2]-resultado[4]
    resultado[9]=cont[9]-resultado[5]-resultado[6]-resultado[8]
    print(resultado)
    res=''
    for k in range(10):
        if resultado[k]>0:           
            res=res+str(k)*resultado[k]
    d = 'Case #'+str(i+1)+': '+res
    print(d)
    out_file.write(d+'\n')
out_file.close()
in_file.close()


