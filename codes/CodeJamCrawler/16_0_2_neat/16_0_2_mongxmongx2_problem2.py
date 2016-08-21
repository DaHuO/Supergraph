import fileinput

def pan_cake(Cake):

    count = 0
    for i in range(len(Cake)):
        if Cake[len(Cake)-1-i] == 0:
            for j in range(len(Cake)-1-i):
                if Cake[j] == 1:
                    Cake[j] = 0
                else:
                    Cake[j] = 1
            count += 1
    
    return count

if __name__ == "__main__":

    input_file = open("B-large.in")
    output_file = open("B-large.out","w")

    T  = int(input_file.readline())
    #T  = input()
    result_array = []
    
    for i in range(T):
        Input = input_file.readline()
        #Input = raw_input()
        Cake = []
        for j in range(len(Input)):
            if Input[j] == "+":
                Cake.append(1)
            elif Input[j] == "-":
                Cake.append(0)
        result = pan_cake(Cake)
        result_array.append(result)
            
    for i in range(T):
        #print("Case #"+str(i+1)+": " + str(result_array[i]))
        output_file.write("Case #"+str(i+1)+": " + str(result_array[i]) + "\n")
    output_file.close()
    
