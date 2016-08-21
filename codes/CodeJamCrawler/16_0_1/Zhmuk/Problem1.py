################## Elena Khusainova #####################

################## Libraries ############################


######################### Main ##########################
filename = "A-large.in"

f = open(filename, "r")
data = f.read()
f.close()

data = data.split("\n")

data_list = []
for i in data:
    try:
        i = int(i)
        data_list += [i]
    except:
        pass



T = data_list[0]
data_list.remove(T)

digits = set(list('0123456789'))

for i in range(T):
    app = []
    mult = 1
    while digits.difference(set(app)) and mult <= 100:
        temp = data_list[i] * mult
        app += list(str(temp))
        mult += 1
    if digits.difference(set(app)):
        with open("Problem1Large_out.txt", "a") as myfile:
            myfile.write('Case #'+str(i+1)+': INSOMNIA'+'\n')
        myfile.close()
    else:
        with open("Problem1Large_out.txt", "a") as myfile:
            myfile.write('Case #'+str(i+1)+': ' + str(temp)+'\n')
        myfile.close()
        

