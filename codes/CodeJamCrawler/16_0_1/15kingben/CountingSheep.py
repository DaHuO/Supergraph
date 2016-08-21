from __future__ import print_function

output = open("output.txt", "w")

with open("input.txt") as f:
    lines = f.readlines()
    length = int(lines[0].split()[0])
    for i in range(0, length):
        startNum = int(lines[1+i].split()[0])
        if(startNum == 0):
            outline = "Case #" + str( i + 1) +  ": " +  "INSOMNIA"
            output.write(outline)
            output.write("\n")
        else:
            dic = {1 : False, 2 : False, 3 : False, 4 : False, 5 : False, 6 : False, 7 : False, 8 : False, 9 : False, 0 : False }
            numSat = 0;
            count = 1
            while(numSat < 10):
                #loop through digits
                num = startNum * count
                temp = num
                while(temp > 0):
                    if(dic[temp % 10] == False):
                        numSat += 1
                        dic[temp % 10] = True
                    temp = temp // 10
                count+=1

            outline = "Case #" + str( i + 1) +  ": " +  str(num)
            output.write(outline)
            output.write("\n")
