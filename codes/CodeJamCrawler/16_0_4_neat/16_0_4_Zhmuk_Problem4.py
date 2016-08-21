################## Elena Khusainova #####################

################## Libraries ############################


######################### Main ##########################
filename = "D-small-attempt0.in"

f = open(filename, "r")
data = f.read()
f.close()

data = data.split("\n")

T = data[0]
data.remove(T)

data_list = []
for i in data:
    temp = i.split(' ')
    if len(temp) == 3:
        data_list += [temp]



for i in range(int(T)):
    K = int(data_list[i][0])
    C = int(data_list[i][1])

    answer = []
    for j in range(1,K+1):
        pos = j
        for c in range(C-1):
            pos = (pos-1) * K + j 
        answer += [str(pos)]

    with open("Problem4Small_out.txt", "a") as myfile:
        myfile.write('Case #'+str(i+1)+': ' + ' '.join(answer) +'\n')
    myfile.close()
        
        

