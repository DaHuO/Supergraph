def giveCount(number):
    if number==0:
        return "INSOMNIA"
    number_list = []
    for i in range(10):
        number_list.append(i)

    i = 1
    while(len(number_list)!=0):
        num = number * i
        for char in str(num):
            if int(char) in number_list:
                number_list.remove(int(char))
        i+=1
    return num

f = open("firstText.txt", "r")
f_out = open("output.txt","w")

inputs = int(f.readline())
i = 1

while(inputs!=0):
    f_out.write("Case #"+str(i)+": "+str(giveCount(int(f.readline())))+"\n")
    inputs-=1
    i+=1

for line in f:
    print ""
                

f.close()
f_out.close()
