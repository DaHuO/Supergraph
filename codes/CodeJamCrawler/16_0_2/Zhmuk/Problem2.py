################## Elena Khusainova #####################

################## Libraries ############################


######################### Main ##########################
filename = "B-large.in"

f = open(filename, "r")
data = f.read()
f.close()

data = data.split("\n")

data_list = []
for i in data:
    try:
        data_list += [i]
    except:
        pass

T = data_list[0]
data_list.remove(T)



for i in range(int(T)):
    curr = list(data_list[i])
    temp = 0
    while len(curr):
        sgn = curr[0]
        while curr and curr[0] == sgn:
            curr.remove(sgn)
        temp += 1

    if sgn == '-':
        temp += 1

    with open("Problem2Large_out.txt", "a") as myfile:
        myfile.write('Case #'+str(i+1)+': ' + str(temp-1)+'\n')
    myfile.close()
        

