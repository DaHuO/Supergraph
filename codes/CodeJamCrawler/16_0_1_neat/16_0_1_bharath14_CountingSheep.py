__author__ = 'bharath'

count=0
arr=[0]*10

def find_digits(n):
    global count
    while n>0:
        if arr[n%10]==0:
            count+=1
            arr[n%10]+=1
        n=n/10

def main():
    t=input()
    for i in range(0,t):
        global count
        count=0
        global arr
        arr=[0]*10
        n=input()
        s=n
        if n==0:
            print "Case #%d: INSOMNIA"%(i+1)
            continue
        m=1
        while count!=10:
            n=s*m
            m+=1
            find_digits(n)
        print "Case #%d: "%(i+1)+str(n)
if __name__ == "__main__":
    main()