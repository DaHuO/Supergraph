import numpy as np

# ---- config ---- #

FileInput="dataPancakesLarge.in"
FileOutput="dataPancakesLarge.out"

# ---------------- #

def start(pancakes):
    pancakes=pancakes[::-1]
    pan=[]
    turns=0
    for p in pancakes:
        pan.append(p)
    i=0
    for p in pan:
        if p=="-":
            pan=turn_pancakes(pan,i)
            turns=turns+1
        i=i+1
    return str(turns)
    
def build_pancakes(pan):
    pancakes=""
    for p in pan:
        pancakes=pancakes+p
    return pancakes

def turn_pancakes(pan,start):
    i=0
    for p in pan:
        if i>=start:
            if pan[i]=="-":
                pan[i]="+"
            else:
                pan[i]="-"
        i=i+1
    return pan
    
def file_load():
    check=[]
    with open(FileInput) as f:
        for line in f:
            check.append(line)
    return check

def normal_mode():
    result = start("+-+")
    print "------------------------------------"
    print "Result: "+str(result)
    print "------------------------------------"
        
def array_mode():
    f = open(FileOutput, 'w')
    check = file_load()
    print check
    for i in range(np.size(check)):
        if i>0:
            writeString = "Case #"+str(i)+": "+str(start(str(check[i]).replace("\n","")))
            f.write(writeString+"\n")
            print writeString
    print "------------------------------------"
    f.close()
                       
if __name__ == "__main__":
    print "------------------------------------"
    print "Start program"
    print "------------------------------------"
    array_mode()