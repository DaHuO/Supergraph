input_file_name = "A-large"
output_file=open("{}.out" .format(input_file_name),'a')
check = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def getSheepSleep(N):
    temp = set([])
    sleep = False
    for i in xrange(1, 100000000):
        out = i * N
        temp = temp.union(set(map(int,str(out))))
        if all(x in temp for x in check):
            sleep = True
            # print out
            break
    if not sleep:
        return "INSOMNIA"
    else:
        return out

with open("{}.in".format(input_file_name)) as input_file:
    counter= 0
    try:
        totalInput=long(input_file.readline())
        for i in range(totalInput):
            value=getSheepSleep(long(input_file.readline()))
            if i==totalInput-1:
                output_file.write("Case #{}: ".format(i+1)+str(value))
            else:
                output_file.write("Case #{}: ".format(i+1)+str(value)+"\n")
    except Exception as e:
        pass


print "done"
output_file.close()



