file = open('C:\\Users\\V\\Downloads\\B-large.in','r')
f = file.read()
res = f.split("\n")

#print res
T = int(res[0])
#T = int(input())
#print T
file.close()
file = open('C:\\Users\\V\\Downloads\\Google2large.out','w')
for j in range(0, T):
    #s = str(raw_input())
    s = str(res[j + 1])
    i = 0
    count = 0
    while i < len(s):
        if s[i] == '-':
            count = count + 2
            while i < len(s) and s[i] == '-':
                i = i + 1
            if i >= len(s):
                break
            #else:
             #   if k > 0:
            #       count = count + 1
        i = i + 1    
    if s[0] == '-':
        count = count - 1
    #if s[len(s) - 1] == '-':
        #count = count - 1
    print count        
    file.write("Case #" + str(j + 1) + ": " + str(count) + "\n")
    #s = str(res[i + 1])
    
file.close()        