file1 = open(r"C:\Users\Wu Jui Hsuan\Desktop\DS.txt","r")
file = open(r"C:\Users\Wu Jui Hsuan\Desktop\gjmi.txt","w")

def power(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b % 2 == 0:
        return power(a*a,b//2)
    else:
        return power(a*a,b//2)*a
        
#T = int(input())
T = int(file1.readline())
for i in range(T):
    k,c,s = map(int,file1.readline().split())
    #k,c,s = map(int,input().split())
    r = ' '.join([str(power(k,c-1)*j+1) for j in range(k)])
    file.write("Case #%d: %s\n" % (i+1,r))
    print("Case #%d: %s\n" % (i+1,r))
        
            

            
            
            
    