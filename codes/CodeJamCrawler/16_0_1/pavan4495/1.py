def my_fun(x):
        a=[]
        k=1
        global m
        m=x
        def gen_list(x,a,k):
                summ=0
                a+=([int(i)for i in str(x)])
                a=list(set(a))
                for z in range(1,len(a)):
                        summ+=a[z]
                x=m
                avg=summ/10
                if avg!=4.5:
                        global p
                        k=k+1
                        p=x*k
                        return gen_list(p,a,k)
                else:
                        return p
        if x==0:
                return "INSOMNIA"
        else:
                return gen_list(x,a,k)

t = int(input())
ko=[]
for i in range(0, t):
        ko.append(int(input()))
for i in range(0,t):
        sdf=my_fun(ko[i])
        print("Case #{}: {}".format(i+1, sdf))
