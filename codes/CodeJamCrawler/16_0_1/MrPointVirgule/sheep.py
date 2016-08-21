t = int(input())
for i in range(1,t+1):
    n=int(input())
    if n==0:
        reponse="INSOMNIA"
    else:
        nb=0
        digits={}
        while not ('0' in digits and '1' in digits and '2' in digits and '3' in digits and '4' in digits and '5' in digits and '6' in digits and '7' in digits and '8' in digits and '9' in digits) :
            nb+=n
            for c in str(nb):
                digits[c]=True
        reponse=nb
    print("Case #"+str(i)+": "+str(reponse))