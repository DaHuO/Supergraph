f = open("/Users/KOCABEY/Desktop/u.in")
data = f.readlines()
f.close()
f = open("/Users/KOCABEY/Desktop/u.txt","w")
test_number = int(data[0])

for i in range(test_number):
    f.write("Case #" + str(i+1) + ": ")
    test = list(data[i+1])
    def flip(N):
        global test
        for i in range(N):
            if test[i] == "+":
                test[i] = "-"
            else:
                test[i] = "+"

    ctr = 0

    for i in range(len(test)):
        if test[len(test) - i - 1] == "-":
            flip(len(test) - i)
            ctr += 1

    f.write(str(ctr) + "\n")

f.close()
