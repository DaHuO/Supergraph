def print_last(N):

    digit_list = ['0','1','2','3','4','5','6','7','8','9']

    i = 1
    n_str = ""
    while digit_list:
        n_str = str(N * i)
        for c in n_str:
            #print c
            try:
                digit_list.remove(c)
            except ValueError:
                pass
        #print n_str
        #print digit_list
            
        i += 1


    print n_str
    #print i


T = int(raw_input())

for i in range(T):
    N = int(raw_input())
    if(N == 0):
        print "Case #" + str(i+1) + ": INSOMNIA"
    else:
        print "Case #" + str(i+1) + ":",
        print_last(N)



