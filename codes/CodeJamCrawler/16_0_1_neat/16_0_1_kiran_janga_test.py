n = input()

result = ""

for w in range(n):
    l = [0,1,2,3,4,5,6,7,8,9]
    a = raw_input()
    if (int(a)==0):
        result+="Case #" + str(w+1)+":"+" INSOMNIA"+"\n"
    else:
        i = 1
        f = 1
        while (len(l)!=0):
            f = i*int(a)
            for p in str(f):
                if int(p) in l:
                    l.remove(int(p))

            i+=1
        result+="Case #" + str(w+1)+": "+str(f)+"\n"

print result
