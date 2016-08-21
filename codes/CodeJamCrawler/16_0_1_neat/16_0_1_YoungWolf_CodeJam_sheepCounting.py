#Problem: Counting Sheep
#Author: Somdeep Datta


digit=[0,1,2,3,4,5,6,7,8,9]
count_digit=[]

def count(n,j):
    count_digit.sort()
    try:
        if digit == count_digit:
            return n*(j-1)

        else:
            for i in range(10):
                if str(digit[i]) in  str(n*j):
                    if(digit[i]) not in count_digit:
                        count_digit.append(digit[i])
            return count(n,j+1)

    except RecursionError:
        return ("Insomnia")

t=int(input())
for i in range(1, t + 1):
        count_digit=[]
        n=int(input())
        case=count(n,1)
        print("Case #{}: {}\n".format(i, case))
