
def counting_sheep(n):
    if n==0:
        return "INSOMNIA"
    s = set(str(n))
    val = n
    while len(s)<10:
        val += n
        s |= set(str(val))
    return val
        
    

    
n = int(raw_input())
for i in range(n):
    start = eval(raw_input())
    sheep = counting_sheep(start)
    print "Case #{0}: {1}".format(i+1, sheep)
    
