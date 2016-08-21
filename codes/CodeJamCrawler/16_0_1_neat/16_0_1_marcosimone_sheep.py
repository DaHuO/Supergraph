found=[0,0,0,0,0,0,0,0,0,0]
inputfile=open('sheep_input')
input=inputfile.read()
numbers=input.split('\r\n')
numbers.remove(numbers[0])
for index,num in enumerate(numbers):
    tmp=int(num)
    count=1
    while 1:
        if tmp==0:
            print "Case #%d: INSOMNIA" % (index+1)
            break
        for char in str(tmp):
            found[int(char)]=1
        if 0 not in found:
            print "Case #%d: %d" % (index+1,tmp)
            found=[0,0,0,0,0,0,0,0,0,0]
            break
        else:
            tmp=int(num)*count
            count+=1