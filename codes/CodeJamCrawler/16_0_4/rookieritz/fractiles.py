file = open('D-small-attempt0.in', 'r+')
file_output= open('output.txt','w+')

test_cases=int(file.readline())
for i in range(1,test_cases+1):
    file_output.write("Case #{}: ".format(i))
    fractile=file.readline()
    k=int(fractile.split(' ')[0])
    c=int(fractile.split(' ')[1])
    s=int(fractile.split(' ')[2])
    for l in range(1,k+1):
        file_output.write(str(l))
        if (l!=test_cases):
            file_output.write(" ")
    if(i!=test_cases):
        file_output.write("\n")

file.close()
file_output.close()
