
fo = open("2016A-large.in", "r")
f = open("2016A-large.out", "w")
lines=fo.readlines() #reads each line of the input data and stores it in array form
cases = int(lines[0]) #first entry of any input data tells you how many data points there are

for n in range(0, cases): #looking at each set of input data

    input = int(lines[n+1]) #changes data type, since all data is read as a string and not a number

    array = [0]*10 #keeps track of whether each digit has already appeared
    compare = [1]*10
    multiple = 1

    while (array != compare) & (input != 0):
        current = str(multiple * input)
        for letters in current:
            currentdigit = int(letters)
            array[currentdigit] = 1
            #f.write(str(currentdigit))
            #f.write("SPACE")
        multiple = multiple + 1
    

    if n !=0:
        if input == 0: #the only time you get insomnia is when the number is 0
            f.write("\nCase #{}: INSOMNIA".format(n+1))
        else:
            f.write("\nCase #{}: {}".format(n+1, current))
    else:
        if input == 0:
            f.write("Case #{}: INSOMNIA".format(n+1))
        else:
            f.write("Case #{}: {}".format(n+1, current))



fo.close()
f.close()
