last_num = 0
def counting_sheep(count, number, numbers, case):
    global last_num
    if number == 0:
        print "Case #"+str(case)+": INSOMNIA"
    else:
        if len(numbers) != 0:
            num = str(count * number)
            for n in num:
                if int(n) in numbers:
                    numbers.remove(int(n))
                    last_num = num
            count += 1
            counting_sheep(count, number, numbers, case)
        else:
            print "Case #"+str(case)+": "+str(last_num)


fo = open("A-large.in", "rw+")
line = fo.readlines()
lines = [x.split('\n')[0] for x in line]
lines.pop(0)

count = 0
for case in lines:
    count += 1
    num = counting_sheep(1, int(case), [0,1,2,3,4,5,6,7,8,9], count)
