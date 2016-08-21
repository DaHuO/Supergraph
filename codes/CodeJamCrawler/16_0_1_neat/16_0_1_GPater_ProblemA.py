import fileinput

def check():
	return 0

def printSet():
	print ("set is ...")

def testSet(genericSet):
        counter = 0
        for x in genericSet:
                print (x)
                counter+=x
        print ("Counter = " , counter)




def main(N):
        setIsNotCompleted = 1
        setTobeCheck = set()
        if(N==0):
                return 'INSOMNIA'  
                print (setTobeCheck)
        else:
                i=0                 
                while(setIsNotCompleted):
                        splittedN = ([int(i) for i in str((i+1)*N)])
                        for x in splittedN:                                
                                setTobeCheck.add(x)
                        i += 1
                        if len(setTobeCheck)==10:
                                setIsNotCompleted=0                        
                return (i)*N

               
def read():
        t = int(input())
        for i in range(1, t + 1):
                #print(input())
                print("Case #{}: {}".format(i, main(int(input()))) )

 

read()

