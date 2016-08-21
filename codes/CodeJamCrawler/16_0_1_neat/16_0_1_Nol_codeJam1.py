#!/usr/bin/env python3

# function which return the digit of a number N in base10 as a list of character
def  digitfrom(N):
    return list(set(str(N))) 

# function that return the last number compute until we find all 10 digits  as string 
# return INSOMNIA in case of 0
# we assume that for any Natural number U0,  for any 'a'of {0,1,2,3,4,5,6,7,8,9} there is n such as 'a' is a digit of U0*n
def sleepy(N):
    print("sleepy count for seed : " + str(N))
    if N==0:
        return "INSOMNIA"
    digitlist=digitfrom(N)
    print("first digit list :" + str(digitlist))
    size=len(digitlist)
    i=1
    A=N
    while size!=10:#We stop when our list contain all 10 digits
        i=i+1
        A=i*N
        dl=digitfrom(A)
        digitlist=list(set(digitlist)|set(dl))#we create a new list containing digit both in our precedent list and in the new number
        size=len(digitlist)
        print("digit list apres avoir compter les digit de : "+str(i*N))
        print(digitlist)
    return str(A)
    pass

def main():
    inFile=open("dataset.txt",'r')
    outFile=open("output.txt",'w')
    caseNumber=int(inFile.readline())
    print("number of case :" + str(caseNumber))
    i=1
    for line in inFile:
        N=int(line)
        outFile.write("Case #"+str(i)+": "+sleepy(N)+'\n');
        i=i+1
    inFile.close()
    outFile.close()
    pass


main()
