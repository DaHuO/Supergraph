arr = []

with open("A-large.in") as f:
    n = int(f.readline())
    #print(n)
    for i in range(n):
        x = int(f.readline())
        arr.append(x)

fo = open('output.out', 'w')

def evaluate(i, index):
    digits = []
    digits = list(set(str(i)))
    contor = 2
    while(len(digits)!=10):
        inc = contor * i
        digits= list(set( digits + list(set(str(inc)))))
        contor+=1
    fo.write("Case #{}: ".format(index) + str(inc)+ "\n")
    
    

    
#print(arr)

for i in range(n):
    if arr[i]==0: fo.write("Case #{}: INSOMNIA".format(i+1) + "\n")
    else:   
        evaluate(arr[i], i+1)
   
fo.close()
    
    