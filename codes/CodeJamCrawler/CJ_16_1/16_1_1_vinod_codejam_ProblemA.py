
#array=[]
#lastWord="ZXCASDQWE"
MAX=None
lastWord=None
def fun(str):
    global MAX,lastWord
    if len(str)==len(lastWord):
       
        if MAX<str:
            MAX=str
        return str
    fun(str+lastWord[len(str)])
    fun(lastWord[len(str)]+str)


output_file=open("solutionA.out",'a')

with open("A-small-attempt0.in") as input_file:
    counter=0
    totalInput=long(input_file.readline())
    for i in range(totalInput):
        lastWord=input_file.readline()
        MAX=lastWord
        fun(lastWord[0])
        if i==totalInput-1:
            output_file.write("Case #{}: ".format(i+1)+MAX.rstrip('\r\n'))
        else:
            output_file.write("Case #{}: ".format(i+1)+MAX.rstrip('\r\n')+"\n")
    
print "done"
output_file.close()


