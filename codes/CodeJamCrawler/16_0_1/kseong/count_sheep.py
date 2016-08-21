import sys

def get_last_no(sheep):
    if sheep<=0:
        return "INSOMNIA"
    
    n = sheep
    cnt=1
    max_n = sys.maxint
    arrDigit = [False,False,False,False,False,
                False,False,False,False,False]

    while (n < max_n):
        digits = map(int, str(n))
        digit_set = set(digits)

        for ds in digit_set:
            arrDigit[ds] = True

        if sum(arrDigit)==10:
            break

        cnt += 1
        n = cnt*sheep

    return str(n)


f=open('A-large.in','r')
fo=open('A-large.out','w')

total_test_cases = int(f.readline().strip('\n'))
test_case_count = 1

e = f.readline()
while (test_case_count <= total_test_cases):
    i = int(e.strip('\n'))
    s_answer = get_last_no(i)

    fo.write('Case #'+ str(test_case_count)+ ': '+ s_answer + '\n')
    test_case_count = test_case_count + 1
  
    e = f.readline()
    if (not e):
        break

f.close()
fo.close()
print 'Done Count Sheep!'

#for i in range(0,1000000+1):
#    print "Last number of ",i," = ",get_last_no(i)
    
