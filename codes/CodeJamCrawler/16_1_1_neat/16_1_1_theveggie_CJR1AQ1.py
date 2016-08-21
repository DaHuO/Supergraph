import sys
sys.setrecursionlimit(1800000)

file=open('A-large (1).in','r')
file1=open('output-q1.txt','w')


results=[]
answer=''

for j in range(1,int(file.readline())+1):
    word=file.readline().strip("\n")
    answer=word[0]
    for i in word[1:]:
        if ord(i)>=ord(answer[0]):
            answer=i+answer
        else:
            answer+=i
    print("Case #%d: %s" % (j,answer))
    file1.write("Case #%d: %s\n" % (j,answer))
    #print('\n\n\n')

file.close()
file1.close()
