__author__ = 'adilmezghouti'

# for j in "12345":
#     print j

#reading a the input file
with open("input.txt","r") as f:
    cases = f.readline()
    product = 0

    for i in range(0,int(cases),1):
        numbers = "0123456789"
        N = int(f.readline())
        counter = 1

        while True:
            # product = c*counter
            if N == 0:
                print "Case #" + str(i + 1) + ": INSOMNIA"
                break

            for j in str(N*counter):
                # print j
                numbers = numbers.replace(j,"")

            # print N
            # print numbers
            if numbers == "":
                print "Case #" + str(i + 1) + ": " + str(N*counter)
                break
            else:
                counter += 1
#
#
# #writing to the output file
# with open("output.txt","w") as output:
#     output.write("This is a test")
#     output.writelines("This is a test")
#     output.writelines("This is a test")
