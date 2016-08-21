def digits_of(num):
    return list(str(num))

file_in = open("A-large.in")
file_out = open("submit.out", "w")
tc = int(file_in.readline())
j = tc+1
while tc:
    i = 1
    n = int(file_in.readline())
    if n == 0:
        file_out.write("Case #{0}: INSOMNIA\n".format(j-tc))
    else:
        check_list = [False]*10
        flag = True
        while flag:
            num = i*n
##            print("num = ", num,"\ti = ", i)
            tmp = digits_of(num)
            for m in tmp:
                check_list[int(m)] = True
##                print(m, " = True")
                
##            print("Out of first for loop")
            for m in check_list:
                if m is False:
                    break
            else:
                
                file_out.write("Case #{0}: {1}\n".format(j-tc, num))
                flag = False
                break
            i += 1
##            print("i = ", i)
    tc -= 1
file_in.close()
file_out.close()
