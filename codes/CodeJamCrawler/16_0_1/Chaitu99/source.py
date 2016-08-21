t = int(input())
input_list = []
for j in range(1, t + 1):
    ip = int(input())
    input_list.append(ip) 
    
for n in input_list:
    if n==0:
        print("Case #{}: {}".format(input_list.index(n)+1, "INSOMNIA"))
    else :
        req = ['0','1','2','3','4','5','6','7','8','9']
        available = list(str(n))
        i=2
        m=i*n
        while not list(set(sorted(req))) == list(set(sorted(available))) :
            m = i*n
            temp = list(str(m))
            for x in temp:
                available.extend(x)
            i = i+1
        print("Case #{}: {}".format(input_list.index(n)+1, m))
