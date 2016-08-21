__author__ = 'bharath'
def main():
    t=input()
    alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(1,t+1):
        print "Case #%d:"%(i),
        n = input()
        arr = list(map(int,raw_input().split(" ")))
        sum =0
        for i in arr:
            sum+=i
        while sum>0:
            if(sum==3):
                max1=0
                for j in range(1,len(arr)):
                    if arr[j]>arr[max1]:
                        max1=j
                print alp[max1],
                arr[max1]-=1
                sum-=1
            else:
                if arr[0]>arr[1]:
                    max1=0
                    max2=1
                else:
                    max1=1
                    max2=0
                for j in range(2,len(arr)):
                    if arr[j]>arr[max2]:
                        if(arr[j]>arr[max1]):
                            max2=max1
                            max1=j
                        else:
                            max2=j
                print alp[max1] + alp[max2],
                arr[max1]-=1
                arr[max2]-=1
                sum-=2
        print

if __name__=="__main__":
    main()
