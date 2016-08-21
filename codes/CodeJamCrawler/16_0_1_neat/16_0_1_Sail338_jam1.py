li_to_9 = []
file = open('small_in.in','rb')
w_file = open('output.txt','wb')
cases = file.readline()
p_cases = 1
m = 1
for line in file:
    n = int(line)
    #scan n
    if n ==0:
        w_file.write("Case #" + str(p_cases) + ":" + " " + "INSOMNIA\n")
        p_cases +=1
        continue

    multiplier = 1
    li = []
    check = [0,1,2,3,4,5,6,7,8,9]
    check = set(check)
    li = set(li)

    for i in str (n):
        li.add(int(i))
    #check list
    while li != check:
        m = multiplier * n
        print n 
        for i in str(m):
            print m
            li.add(int(i))
        multiplier +=1


    #now we have our list
    w_file.write("Case #" + str(p_cases) + ": "  + str(str(m) +' \n'))
    li = []
    p_cases +=1
    multiplier = 1
    m = 1 

w_file.close()
file.close()

