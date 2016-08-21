def flip(read,pos):
    while pos>=0:
        if read[pos]=='-':
            read[pos]='+'
        elif read[pos]=='+':
            read[pos]='-'
        
        pos=pos-1
            
def calculate(read,iterations):
    pos=len(read)-1
    final=0
    while (pos!=-1 or read[0]!="+"):
       
        if (read[pos]=="-"):
            flip(read,pos)
            final=final+1
        pos=pos-1
        
    #print("---",read)
    print("Case #{}: {}".format(iterations,final))



    
if __name__=="__main__":
    
    import sys
    sys.stdin.readline()
    iterations=1
    read=sys.stdin.readline()

    while (read!=""):

        if(read[-1:]=="\n"):
            read=read[:-1]
            
        calculate(list(read),iterations)
        iterations=iterations+1
        read=sys.stdin.readline()
        
