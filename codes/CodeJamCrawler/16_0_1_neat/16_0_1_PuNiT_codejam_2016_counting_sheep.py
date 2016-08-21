###AUTHOR:PUNIT PATEL
test_case=int(raw_input())
i=1
while(i<=test_case):
    iterator=2
    number=int(raw_input())
    temp=number
    if number==0:
        print "Case #" + str(i) + ": INSOMNIA"
    else:
        string=str(temp)
        while(1):
            if(len(set(string))==10):
                print"Case #" + str(i) + ": "+str(temp_number)
                break
            else:
                temp_number=number*iterator
                string+=str(temp_number)
                iterator+=1
    i+=1
