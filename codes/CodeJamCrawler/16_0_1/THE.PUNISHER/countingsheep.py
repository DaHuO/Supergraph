
def func(orig):
    if orig==0:
        return 'INSOMNIA'
    map = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    total = 0
    num=orig

    while True:
        num2 = num
        while num2:
            digit = num2%10
            if(map[digit]==0):
                map[digit]=1
                total+=1
            if total==10:
                return num
            num2//=10
        num += orig


lines = [int(line.rstrip('\n')) for line in open('small_countingsheep')]
i=1
for line in lines[1:len(lines)]:
    k = str(i)
    print 'Case #'+k+':',func(line)
    i+=1