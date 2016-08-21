import re
import math
import itertools

def divs(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor
        
def s2d(given,target):
    #given string of binary of base convert to decimal
    num=0
    p=len(given)-1
    exponent=0
    while(p>=0):
        if given[p]=="1":
            num+=target**exponent
        exponent+=1
        p-=1
    return num

def gettry(length):
    length=int(length)
    if length>2:
        length=length-2
        for i in itertools.product([0,1],repeat=length):
            ii=list(i)
            iii = ''.join([str(mli) for mli in ii])
            yield "1"+iii+"1"
    else:
        yield "11"
    return

def main():
    filename="1in.dat"
    output="1out.dat"
    fo=open(output,'w')
    fp=open(filename,'r')
    

    found=[]
    proof=[]
    c=-1
    vals=0
    flag=True
    for line in fp.readlines():
        c+=1
        line=re.sub(r'\n','',line)
        if c>0:
            liner=re.split(r' ',line)
            length=liner[0]
            vals=int(liner[1])
            valids=0
            print "Searching "+str(length)+" vals: "+str(vals)
            
            for line in gettry(length):
#d                print "For------ "+str(line)
                if "1"==line[0] and "1"==line[len(line)-1]:
    
                    base=1
                    divbase={}
                    flag_none_primes=True
                    while(base<10):
                        base+=1
                        result=s2d(line,base)

                        divisor=0
                        for d in divs(result):
                            if d>2 and not d==result:
                                divisor=d
                                break

                            
                        if not divisor==0:
                            divbase[base]=divisor
                            #found.append(result)
                        else:
                            flag_none_primes=False
                            break
                    
                    if flag_none_primes:
                        #Do output
                        valids+=1
                        if flag:
                            fo.write("Case #"+str(valids)+":\n")
                            flag=False
#                        print line+" "
                        fo.write(line)
                        for x in range(2,11):
#                            print str(x)+": "+str(divbase[x])
                            fo.write(" "+str(divbase[x]))
                        fo.write("\n")
#                        print "String "+line+" in base "+str(base)+" is "+str(result)+" divisor: "+str(divisor)+" values: "+str(valids)+" going for "+str(vals)
                if valids>=vals:break
                
    fo.close()
    fp.close()

    return

if __name__ == '__main__':            
    main()
   









