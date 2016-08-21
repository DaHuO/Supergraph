s = open("A-large.in",'r')

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
l=[]
number=0
for i,line in enumerate(s):
    if i > 0:
        l.append(line.rstrip('\n'))
    else:
        number=int(line[:-1])



result=[]
for i in range(number):

    if i >0:
        j += 2
    else:
        j = i

    nbParts = int(l[j])

    parts=[]
    for part in l[j+1].split(' '):
        parts.append(int(part));

    st=[]
    while max(parts) > 0:
        maxi = max(parts);
        indexMaxi = [i for i,item in enumerate(parts) if maxi == item]

        if len(indexMaxi) > 1:
            copyParts = list(parts);
            for ind,val in enumerate(copyParts):
                if val == maxi:
                    copyParts[ind] = 0
            maxiForDist = max(copyParts)
            dist = maxi - maxiForDist
            if dist > 1:
                if len(indexMaxi) % 2 == 0:
                    parts[indexMaxi[0]] -= 1
                    parts[indexMaxi[1]] -= 1
                    st.append(str(alpha[indexMaxi[0]])+str(alpha[indexMaxi[1]]));
                else:
                    parts[indexMaxi[0]] -= 1
                    st.append(str(alpha[indexMaxi[0]]));
            else:
                notInZero = sum([1 for item in copyParts if item > 0])
                if maxi > 1 :
                    if len(indexMaxi) > 2:
                        parts[indexMaxi[0]] -= 2
                        st.append(str(alpha[indexMaxi[0]])+str(alpha[indexMaxi[0]]));
                    else:
                        if len(indexMaxi) % 2 == 0:
                            parts[indexMaxi[0]] -= 1
                            parts[indexMaxi[1]] -= 1
                            st.append(str(alpha[indexMaxi[0]])+str(alpha[indexMaxi[1]]));
                        else:
                            parts[indexMaxi[0]] -= 1
                            st.append(str(alpha[indexMaxi[0]]));
                else:
                    if len(indexMaxi) % 2 == 0:
                        parts[indexMaxi[0]] -= 1
                        parts[indexMaxi[1]] -= 1
                        st.append(str(alpha[indexMaxi[0]])+str(alpha[indexMaxi[1]]));
                    else:
                        parts[indexMaxi[0]] -= 1
                        st.append(str(alpha[indexMaxi[0]]));

        else:
            copyParts = list(parts);
            for ind,val in enumerate(copyParts):
                if val == maxi:
                    copyParts[ind] = 0
            maxiForDist = max(copyParts)
            dist = maxi - maxiForDist
            if dist > 1:
                if parts[indexMaxi[0]] > 1:
                    parts[indexMaxi[0]] -= 2
                    st.append(str(alpha[indexMaxi[0]])+str(alpha[indexMaxi[0]]));
                else:
                    parts[indexMaxi[0]] -= 1
                    st.append(str(alpha[indexMaxi[0]]));
            else:
                parts[indexMaxi[0]] -= 1
                st.append(str(alpha[indexMaxi[0]]));

    result.append(st)

lr=[]

for i,r in enumerate(result):
    lr.append("Case #"+str(i+1)+": " +str(" ".join(r)))


print("\n".join(lr))
file1 = open("ba",'w')
file1.write("\n".join(lr))
