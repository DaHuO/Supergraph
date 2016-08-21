file = open('A-large.in', 'r')

datas = file.readlines()

totalAttempts = datas[0]

all_numbers = []
for line in datas[1:]:
    all_numbers.append(line)

outputFile = open('output.txt', 'a')



def expand(N, myList):
    exp_N = str(N)
    len_N = len(exp_N)
    for x in range(0, len_N):
        digi = exp_N[x]
        if (digi not in myList):
            myList.append(digi)
        
def cmp(soft, hard):
    result = True
    for h1 in hard:
        if(h1 not in soft):
            result = False
    return result
            

 

list1 = ['0','1','2','3','4','5','6','7','8','9']
for indx, N in enumerate(all_numbers):
    if(int(N) != 0):
        orig = int(N)
        iter = 0
        list2 = []
        check = True
        while(check):
            listMatches = cmp(list2, list1)
            if(listMatches == True):
                output = ("Case #%d: %s\n" %(indx+1, N))
                print(output)
                outputFile.write(output,)
                check = False
            else:
                iter = iter + 1
                N = orig * iter
                expand(N, list2)
    else:
        output = ("Case #%d: INSOMNIA\n" %(indx+1))
        print(output)
        outputFile.write(output)


outputFile.close()
