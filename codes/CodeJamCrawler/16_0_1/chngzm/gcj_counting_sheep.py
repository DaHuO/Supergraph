#get number of test cases
test_cases = int(input())
input_array = []
#repeat the process for the number of test cases
for k in range(1, test_cases+1):
    current_input = int(input())
    input_array.append(current_input)
for z in range(1,len(input_array)+1):
    #get number from the sheep
    number = input_array[z-1] 
    #array to store the numbers that have appeared
    number_array = []
    #test the number from 1 to 10 times to see if all the numbers are accounted for
    for i in range(1, 101):
        #current number multipled by N + i
        current_number = str(number * i)
        for j in current_number:
            if j not in number_array:
                number_array.append(j)
        #check to see if all the integers have appeared after this number
        if len(number_array) == 10:
            print ("Case #{0}: {1}".format(z, current_number))
            break
    if len(number_array) != 10:
        print ("Case #{0}: INSOMNIA".format(z))
            
        
