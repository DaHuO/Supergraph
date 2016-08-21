input_file = open('workfile.txt', 'r')
output_file = open('outputfile.txt', 'a')

trials = int(input_file.readline())


for t in range(1,trials+1):
    n=int(input_file.readline())
    #n = int(input("N = "))
    #n=t
    numbers = []

    state = True

    mult = 1

    if n != 0:
        while(state):
            count=0
            numbers += str(n*mult)
            for i in range(10):
                if str(i) in numbers:
                    count+=1
                if count == 10:
                    #print(numbers)
                    #print(n*mult)
                    
                    print("N = " , n, " | ", n*mult)
                    output_file.write("Case #" + str(t) + ": " + str(n*mult) + "\n")
                    state = False
            mult+=1
    else:
        output_file.write("Case #" + str(t) + ": " + "INSOMNIA" + "\n")
        print("N = " , n , " INSOMNIA")
        #print("INSOMNIA")
input_file.close()
output_file.close()
