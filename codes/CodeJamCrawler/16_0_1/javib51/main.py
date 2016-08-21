
def calculate(read,iterations):

    goal={}
    n=1
    aux=0
    final=0

    while (len(goal)<10):
        if(read==0):
            print("Case #{}: INSOMNIA".format(iterations))
            break
        aux=n*read
        
        

        for element in str(aux):
            if not element in goal:
                    goal[element]=None
                    final=aux
        

        n=n+1

    if read!=0:
        print("Case #{}: {}".format(iterations, final))



    #Case #1: INSOMNIA


    
if __name__=="__main__":
    
    import sys
    sys.stdin.readline()
    iterations=1
    read=sys.stdin.readline()

    while (read!=""):

        if(read[-1:]=="\n"):
            read=read[:-1]
        
        calculate(int(read),iterations)
        iterations=iterations+1
        read=sys.stdin.readline()
        
