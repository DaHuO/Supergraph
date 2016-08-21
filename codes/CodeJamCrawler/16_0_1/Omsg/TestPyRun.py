import numpy as np

# ---- config ---- #

FileInput="dataSmall.in"
FileOutput="dataSmall.out"

# ---------------- #

def start(N_start):
    digits = np.asarray([0]*10)
    iteration=0
    N=N_start
    if N==0:
        return "INSOMNIA"
    while check_digits(digits)==0 or N>100000:
        iteration=iteration+1
        N=N_start*(iteration)
        set_digits(digits, N)
        #print str(iteration)+")"+str(N)+" - "+str(check_digits(digits))
    return str(N)
    
def check_digits(digits):
    ready=1
    for i in range(10):
        if(digits[i]==0):
            ready=0
    return ready                  
                       
def set_digits(digits, N):
    while N>0:
        number=N%10
        #print "N: "+str(N)
        digits[number]=1
        N=(N-number)/10
    #print digits
    return digits

def file_load():
    check=[]
    with open(FileInput) as f:
        for line in f:
            check.append(int(line))
    return check

def normal_mode():
    result = start(100)
    print "------------------------------------"
    print "Result: "+result
    print "------------------------------------"
        
def array_mode():
    f = open(FileOutput, 'w')
    check = file_load()
    print check
    for i in range(np.size(check)):
        writeString = "Case #"+str(i)+": "+str(start(check[i]))
        f.write(writeString+"\n")
        print writeString
    print "------------------------------------"
    f.close()
                       
if __name__ == "__main__":
    print "------------------------------------"
    print "Start program"
    print "------------------------------------"
    array_mode()