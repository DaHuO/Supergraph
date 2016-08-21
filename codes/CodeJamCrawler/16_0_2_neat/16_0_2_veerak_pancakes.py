__author__ = 'SATYANARAYANAREDDY'
iter_list = []
for e in range(int(input())):
    iter_list.append(raw_input())

for i in range(len(iter_list)):
    st = []
    for each in iter_list[i]:
        st.append(each)

    notDone = False
    for each in st:
        if each != "+":
            notDone = True
    def flipem(c):
        for n in range(0, c+1):
            if st[n] == "+":
                st[n] = "-"
            else:
                st[n] = "+"

    numflips = 0
    while(notDone):
        #see if string is starting with a -
        if st[0] == "-":
            c=0
            #select the longest stretch of minuses
            while(c+1<=len(st)-1 and st[c+1]=="-"):
                c+=1
            flipem(c)
            numflips+=1
        else:#search for the first -
            c = len(st)
            for t in range(len(st)):
                if (st[t] == "-"):
                    c = t
                    while(c+1 <= len(st)-1 and st[c+1]=="-"):
                        c+=1
                    break
            if c == len(st):
                notDone = False
            else:
                notDone = True
                flipem(c)
                numflips+=1

    print "Case #"+str(i+1)+": "+str(numflips)