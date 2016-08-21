import sys
sys.stdin = open('/home/ravsa/Downloads/A-large.in','r')
sys.stdout = open('output.txt','w')
case = 1
T = int(raw_input())
while T:
    word = raw_input()
    temp = word[0]
    for char in word[1:]:
        if temp[-1] >= char:
            temp = temp + char 
        elif temp[0] <= char:
            temp = char + temp
        else:
            temp = temp + char
    print "Case #%d: %s"%(case,temp)
    case += 1
    T -= 1




