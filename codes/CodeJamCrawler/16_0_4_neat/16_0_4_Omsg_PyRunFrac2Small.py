import numpy as np

# ---- config ---- #

FileInput="dataFracSmall.in"
FileOutput="dataFracSmall.out"
tileL="L"
tileG="G"

# ---------------- #
    
def start(K,C,S):
    counter=1
    result=""
    first=1
    last=K**C
    step=last/K
    for i in range(K):
        if K>1:
            counter=first+step*i+(i)*(step-1)/(K-1)
        else:
            counter=1
        result=result+str(counter)
        if i <(K-1):
            result=result+" "
    return result
              
def file_load():
    check=[]
    with open(FileInput) as f:
        for line in f:
            check.append(str(line).replace("\n",""))
    return check
        
def normal_mode():
    print start(2,1,2)
    
def array_mode():
    print "------------------------------------"
    print "Start program"
    print "------------------------------------"
    f = open(FileOutput, 'w')
    check = file_load()
    print check
    for i in range(np.size(check)):
        if i>0:
            line=check[i].split(" ")
            K=int(line[0])
            C=int(line[1])
            S=int(line[2])
            writeString = "Case #"+str(i)+": "+str(start(K,C,S))
            f.write(writeString+"\n")
            print writeString
    print "------------------------------------"
    f.close()
                       
if __name__ == "__main__":
    array_mode()