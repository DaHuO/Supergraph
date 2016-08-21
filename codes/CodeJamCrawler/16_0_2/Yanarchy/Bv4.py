fin = open("B-large.in")
fout = open("output.txt", "w")

def write_out(case, result):
    fout.write("Case #" + str(case) + ": " + str(result) + "\n")

case = 0
lines = []
for line in fin:
    lines.append(line.strip())
lines = lines[1:]

for data in lines:
    #print(case, data)
    counter = 0
    data = list(data)
    #print(data)
    #flip as many consecutive to + as possible
    #flip +s to bottom
    while "-" in data:
        if data[0] == "-":
            i = 0
            while data[i] == "-":
                data[i] = "+"
                if i < len(data) - 1:
                    i += 1
                else:
                    break
        else:
            i = 0
            while data[i] == "+":
                data[i] = "-"
                if i < len(data) - 1:
                    i += 1
                else:
                    break
        counter += 1
        
##        new_data = []
##        #print(data)
##        if data == ["-"]:
##            data = ["+"]
##            counter = 1
##        else:
##            if data[0] == "+":
##                data[0] = "-"
##                counter += 1
##                #print("test 1")
##            else:
##                data.reverse()
##                i = 0
##                while data[i] == "+":
####                    print("C", i)
####                    print("C", data)
####                    print("C", new_data)
##                    new_data += "+"
##                    #print("C", new_data)
##                    i += 1
##                    #print("test2")
####                print("A", data)
####                print("A", new_data)
##                orig_len = len(data)
##                while len(new_data) < orig_len:
##                    
##                    popped = data.pop()
##                    if popped == "+":
##                        new_data += "-"
##                    else:
##                        new_data += "+"
##                #print("B", data)
##                #print("B", new_data)
##                counter += 1
##                new_data.reverse()
##                #print(data)
##                #print(new_data)
##                data = []
##                for element in new_data:
##                    data.append(element)
    #print(counter)
    case += 1
    write_out(case, counter)

    
##        else:
##            #make first pancake - then flip whole stack
##            if data[0] == "+":
##                data[0] = "-"
##                counter += 1
##            orig_len = len(data)
##            while len(new_data) < orig_len - 1:
##                popped = data.pop()
##                if popped == "+":
##                    new_data += "-"
##                else:
##                    new_data += "+"
##            counter += 1
##            data = new_data
##
fin.close()
fout.close()
