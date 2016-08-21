__author__ = 'nimish'
f = open('A-large.in')
case_no = int(f.readline())
no = []*case_no
case_checks = []*case_no
for i in range(case_no):
    no.insert(i, f.readline())

for i in range(no.__len__()):
     test_no = str(no[i])
     all_no = []*10
     inc=1
     while all_no.__len__()!=10:
           test_no_cpy = str(int(test_no)*inc)
           temp = [int(k) for k in test_no_cpy]
           if temp[0] == 0:
                       test_no_cpy = 'INSOMNIA'
                       break
           else:
                inc = inc+1
                for j in temp:
                    if j in all_no:
                              '''this is nothing'''
                    else:
                        all_no.append(j)
     case_checks.append(test_no_cpy)

for i in range(case_no):
    print("Case #"+str(i+1)+": "+str(case_checks[i]))