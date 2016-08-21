inpt=open("dataset.txt")
num=int(inpt.readline())
for i in range(num):
    (K,C,S) = map(int,inpt.readline().split(" "))
    print "Case #"+str(i+1)+":",[i*pow(K,C-1)+1 for i in range(K)]