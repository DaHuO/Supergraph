try:
    infile = open("A-large.in","r")
    cases = int(infile.readline().rstrip("\n"))
    words = infile.readlines()
    infile.close()

    for i in range(len(words)):
        words[i] = words[i].strip("\n")
    answer = []

    outfile = open("answer.txt","a")

    for i in range(len(words)):
        answerword = ""
        word = words[i]
        swap = []
        for item in range(len(word)):
            if swap == []:
                swap.append(word[item])
            elif ord(word[item]) < ord(swap[0]):
                swap.append(word[item])
            else:
                swap.insert(0,word[item])
        outfile.write("Case #{}: {}\n".format(i+1,"".join(swap)))
    outfile.close()
    
except FileNotFoundError:
    print("Enter correct file name")

