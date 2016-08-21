try:
    infile = open("B-large.in","r")
    cases = int(infile.readline().rstrip("\n"))
    pancakes = infile.readlines()
    infile.close()
    outfile = open("answer.txt","a")

    for items in range(cases):
        count = 0
        item = list(pancakes[items].rstrip("\n"))
        sad = True
        while sad:
            sad = False
            for i in range(len(item)):
                if item[i] == "-":
                    sad = True
                    break
            if item[len(item)-1] == "+" and sad:
                for i in range(len(item)-1, -1, -1):
                    if item[i] == "-":
                        break
                    if item[i] == "+":
                        del item[i]
            elif item[len(item)-1] == "-" and sad:
                if item[0] == "-":
                    item = item[::-1]
                    for i in range(len(item)):
                        if item[i] == "-":
                            item[i] = "+"
                        else:
                            item[i] = "-"
                    count += 1
                else:
                    count += 1
                    for i in range(len(item)-1, -1, -1):
                        if item[i] == "+":
                            break
                        if item[i] == "-":
                            del item[i]
                    count += 1
        outfile.write("Case #{}: {}\n".format(items+1,count))
    outfile.close()
except FileNotFoundError:
    print("Enter correct file name")