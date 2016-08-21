#Sarbajit Saha

import sys

sys.stdout=open("ans1.txt","w")
sys.stdin=open("A1.in","r")

def res(n):
    if (n==0):
        return "INSOMNIA"
    else:
        digits = set()
        i=1
        temp = 1
        while(len(digits)!=10):
            temp = str(i*n)
            for t in temp:
                digits.add(t)
            i+=1
        return temp

def main():
    t=int(input())
    for i in range(t):
        n=int(input())
        print ("Case #"+str(i+1)+": "+str(res(n)))

main()
