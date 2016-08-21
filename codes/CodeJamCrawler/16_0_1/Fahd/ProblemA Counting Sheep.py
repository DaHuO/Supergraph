T = input()
def check(N,a):
    if N == 100:
        return "INSOMNIA"
    if "1" in a and "2" in a and "3" in a and "4" in a and "5" in a and "6" in a and "7" in a and "8" in a and "9" in a and "0" in a:
        return int(n)*N
    else:
        return  check(N+1,str(int(n)*(N+1))+a)
for z in range(1,T+1):
    n = input()
    t = check(1,str(n))
    ans= "Case #%i: %s" %(z, t)
    print ans
