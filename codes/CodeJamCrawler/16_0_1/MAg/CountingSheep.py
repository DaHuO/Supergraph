## Maneesh Agarwal
## April 8, 2016
## Counting Sheep

def Call_Me() :
    ib_f = open('ib_Sheep_s.txt','r')
    ob_f = open('ob_Sheep_s.txt','w')
    T = int(ib_f.readline().rstrip('\n'))
    for i in range(1,T+1) :
        Count_Sheep(ib_f,ob_f,i)
        

def Count_Sheep(ib_f, ob_f,c_index) :
    final_str = set('0123456789')
    N = int(ib_f.readline().rstrip('\n'))
    if N == 0 :
        num_str = 'INSOMNIA'
    else :
        Flag = 0
        inc = 1
        s = set("")
        while Flag == 0 :
            
            num_str = str(inc*N)
            s=s.union(set(num_str))# get unique numbers 
            if all(elm in s for elm in final_str):
                #compare all elements of string
                #print 'Case #'+str(i+1)+': ' + num_str
                Flag = 1
            inc += 1
                
    ob_f.write("Case #{}: {}\n".format(c_index, num_str))
    return

if __name__ == '__main__':    
    Call_Me()
