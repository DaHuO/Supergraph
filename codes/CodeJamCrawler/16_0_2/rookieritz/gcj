file = open('B-large.in', 'r+')
file_output= open('output.txt','w+')

pancake=""

test_cases=int(file.readline())
print(test_cases)
for i in range(1,test_cases+1):
    file_output.write("Case #{}: ".format(i))
    pancake=file.readline()[::-1]
    x='-'
    count=0
    for sign in pancake:
        if(sign==x):
            count+=1
            if(x=='-'):
                x='+'
            else:
                x='-'
    file_output.write(str(count))
    if(i!=test_cases):
        file_output.write("\n")

file.close()
file_output.close()
