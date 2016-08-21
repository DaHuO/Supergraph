T=int(input())
for i in range (T):
    S=input()
    count=0
    if S[0]=="-":
        count=-1
    prev="+"
    for char in S:
        if char=="-" and prev=="+":
            count+=2
        prev=char
    print ("Case #" + str(i+1) + ": " + str(count))
