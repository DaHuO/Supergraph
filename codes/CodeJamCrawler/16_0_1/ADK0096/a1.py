a = []
n = 0
def inp():
    global a,n
    n = int(input())
    for i in range(n):
            a.append(int(input()))

def p(x):
    al = [0,0,0,0,0,0,0,0,0,0]
    if(x==0):
        return "INSOMNIA"
    fn = x;
    m = 1
    while(al.count(0) != 0):
        fn = x*m        
        m += 1
        for i in str(fn):
            al[int(i)%10] += 1
    return fn

def main():
    inp()
    for i in range(n):
        print("Case #",i+1,": ",p(a[i]),sep='')

main()

        
        

    
    

