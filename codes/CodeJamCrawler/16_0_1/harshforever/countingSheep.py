__author__ = "Harshit"




def sheepCount(n):
    num_set={'0','1','2','3','4','5','6','7','8','9'}

    i=1


    while i>0:
        new_num = i*n
        set_nums = set(str(new_num))

        num_set = num_set - set_nums
        if num_set==set([]):
            return new_num
        if i > 1000000:
            return "INSOMNIA"
        i+=1


t = int(raw_input())
for i in xrange(0,t):
    num = int(raw_input())
    print "Case #" +str(i+1) + ": " + str(sheepCount(num))