def answer(num):
    if num == 0:
        return "INSOMNIA"
    remaining = [0,1,2,3,4,5,6,7,8,9]
    i = 1
    while len(remaining) !=0 and i <= 10000000:
        curNum = i*num
        for e in remaining[:]:
            if str(e) in str(curNum):
                if e in remaining:
                    remaining.remove(e)  
        i = i + 1
    if len(remaining) == 0:
        return str((i-1)*num)
    else:
        return "INSOMNIA"
    
f = open("C:\Users\Ondrej Bohdal\Downloads\\A-large.in","r")
out = open("C:\Users\Ondrej Bohdal\Downloads\\A-large.out","w")
t = int(f.readline())

e = 0
while e<t:
    out.write("Case #"+str(e+1)+": "+answer(int(f.readline()))+"\n")
    e = e + 1
f.close()
out.close()