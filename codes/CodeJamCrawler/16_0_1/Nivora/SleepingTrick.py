
final_list=[]
def generate_numbers(num):
    x=1
    res=num
    resultList=[]
    if(num==0):
        return "INSOMNIA"
    while not checkDone(resultList):
        res=num*x
        x+=1
        resultList.append([int(d) for d in str(res)])
    resultList=[]
    final_list=[]
    return res

def checkDone(list_of_numbers):
    final_list=[num for elem in list_of_numbers for num in elem]
    result=set(final_list)
    if(len(result)==10):
        return True
    else:
        return False

filename="input.txt"
i=1
with open(filename) as f:
    x=int(f.readline())
    for i in range(1,x+1):
        print("Case #",i,": ",generate_numbers(int(f.readline())))


