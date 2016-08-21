t = int(input())

output = open("output.txt", "w")

for i in range(1, t +1):
    code = input()
    answer = []
    nums = [["Z","E","R","O"], ["O","N","E"], ["T","W","O"], ["T","H","R","E","E"], ["F","O","U","R"], ["F","I","V","E"], ["S","I","X"], ["S","E","V","E","N"], ["E","I","G","H","T"], ["N","I","N","E"]]

    if code.count("Z") > 0:
        highest = 0

        count0 = code.count(nums[0][0])
        count1 = code.count(nums[0][1])
        count2 = code.count(nums[0][2])
        count3 = code.count(nums[0][3])

        highest = count0
        if highest > count1:
            highest = count1
        if highest > count2:
            highest = count2
        if highest > count3:
            highest = count3
        
        for a in range(highest):
            index = code.find(nums[0][0])
            code = code[:index] + code[index+1:]

            index = code.find(nums[0][1])
            code = code[:index] + code[index+1:]

            index = code.find(nums[0][2])
            code = code[:index] + code[index+1:]

            index = code.find(nums[0][3])
            code = code[:index] + code[index+1:]

            answer.append("0")
        
    if code.count("W") > 0:
        highest = 0

        count0 = code.count(nums[2][0])
        count1 = code.count(nums[2][1])
        count2 = code.count(nums[2][2])


        highest = count0
        if highest > count1:
            highest = count1
        if highest > count2:
            highest = count2


        
        for a in range(highest):
            index = code.find(nums[2][0])
            code = code[:index] + code[index+1:]

            index = code.find(nums[2][1])
            code = code[:index] + code[index+1:]

            index = code.find(nums[2][2])
            code = code[:index] + code[index+1:]

            answer.append("2")


    if code.count("U") > 0:
        highest = 0

        count0 = code.count(nums[4][0])
        count1 = code.count(nums[4][1])
        count2 = code.count(nums[4][2])
        count3 = code.count(nums[4][3])

        highest = count0
        if highest > count1:
            highest = count1
        if highest > count2:
            highest = count2
        if highest > count3:
            highest = count3
    
        for a in range(highest):
            index = code.find(nums[4][0])
            code = code[:index] + code[index+1:]

            index = code.find(nums[4][1])
            code = code[:index] + code[index+1:]

            index = code.find(nums[4][2])
            code = code[:index] + code[index+1:]

            index = code.find(nums[4][3])
            code = code[:index] + code[index+1:]

            answer.append("4")

        
    if code.count("X") > 0:
        highest = 0
    
        count0 = code.count(nums[6][0])
        count1 = code.count(nums[6][1])
        count2 = code.count(nums[6][2])


        highest = count0
        if highest > count1:
            highest = count1
        if highest > count2:
            highest = count2


        
        for a in range(highest):
            index = code.find(nums[6][0])
            code = code[:index] + code[index+1:]

            index = code.find(nums[6][1])
            code = code[:index] + code[index+1:]

            index = code.find(nums[6][2])
            code = code[:index] + code[index+1:]

            answer.append("6")


    if code.count("G") > 0:
        highest = 0

        count0 = code.count(nums[8][0])
        count1 = code.count(nums[8][1])
        count2 = code.count(nums[8][2])
        count3 = code.count(nums[8][3])
        count4 = code.count(nums[8][4])


        highest = count0
        if highest > count1:
            highest = count1
        if highest > count2:
            highest = count2
        if highest > count3:
            highest = count3
        if highest > count4:
            highest = count4


        for a in range(highest):
            index = code.find(nums[8][0])
            code = code[:index] + code[index+1:]

            index = code.find(nums[8][1])
            code = code[:index] + code[index+1:]

            index = code.find(nums[8][2])
            code = code[:index] + code[index+1:]

            index = code.find(nums[8][3])
            code = code[:index] + code[index+1:]

            index = code.find(nums[8][4])
            code = code[:index] + code[index+1:]
            
            answer.append("8")


    highest = 0

    count0 = code.count(nums[1][0])
    count1 = code.count(nums[1][1])
    count2 = code.count(nums[1][2])


    highest = count0
    if highest > count1:
        highest = count1
    if highest > count2:
        highest = count2


        
    for a in range(highest):
        index = code.find(nums[1][0])
        code = code[:index] + code[index+1:]

        index = code.find(nums[1][1])
        code = code[:index] + code[index+1:]

        index = code.find(nums[1][2])
        code = code[:index] + code[index+1:]

        answer.append("1")



    highest = 0

    count0 = code.count(nums[3][0])
    count1 = code.count(nums[3][1])
    count2 = code.count(nums[3][2])
    count3 = code.count(nums[3][3])


    highest = count0
    if highest > count1:
        highest = count1
    if highest > count2:
        highest = count2
    if highest > count3//2:
        highest = count3//2
    
    for a in range(highest):
        index = code.find(nums[3][0])
        code = code[:index] + code[index+1:]

        index = code.find(nums[3][1])
        code = code[:index] + code[index+1:]

        index = code.find(nums[3][2])
        code = code[:index] + code[index+1:]

        index = code.find(nums[3][3])
        code = code[:index] + code[index+1:]

        index = code.find(nums[3][4])
        code = code[:index] + code[index+1:]
            
        answer.append("3")





    highest = 0

    count0 = code.count(nums[5][0])
    count1 = code.count(nums[5][1])
    count2 = code.count(nums[5][2])
    count3 = code.count(nums[5][3])

    highest = count0
    if highest > count1:
        highest = count1
    if highest > count2:
        highest = count2
    if highest > count3:
        highest = count3
    
    for a in range(highest):
        index = code.find(nums[5][0])
        code = code[:index] + code[index+1:]

        index = code.find(nums[5][1])
        code = code[:index] + code[index+1:]

        index = code.find(nums[5][2])
        code = code[:index] + code[index+1:]

        index = code.find(nums[5][3])
        code = code[:index] + code[index+1:]

        answer.append("5")







    highest = 0

    count0 = code.count(nums[7][0])
    count1 = code.count(nums[7][1])
    count2 = code.count(nums[7][2])
    count4 = code.count(nums[7][4])


    highest = count0
    if highest > count1//2:
        highest = count1//2
    if highest > count2:
        highest = count2
    if highest > count4:
        highest = count4


        
    for a in range(highest):
        index = code.find(nums[7][0])
        code = code[:index] + code[index+1:]

        index = code.find(nums[7][1])
        code = code[:index] + code[index+1:]

        index = code.find(nums[7][2])
        code = code[:index] + code[index+1:]

        index = code.find(nums[7][3])
        code = code[:index] + code[index+1:]

        index = code.find(nums[7][4])
        code = code[:index] + code[index+1:]
            
        answer.append("7")




    highest = 0

    count0 = code.count(nums[9][0])
    count1 = code.count(nums[9][1])
    count2 = code.count(nums[9][2])
    count3 = code.count(nums[9][3])

    highest = count0
    if highest > count1:
        highest = count1
    if highest > count2:
        highest = count2
    if highest > count3:
        highest = count3
    
    for a in range(highest):
        index = code.find(nums[9][0])
        code = code[:index] + code[index+1:]

        index = code.find(nums[9][1])
        code = code[:index] + code[index+1:]

        index = code.find(nums[9][2])
        code = code[:index] + code[index+1:]

        index = code.find(nums[9][3])
        code = code[:index] + code[index+1:]

        answer.append("9")


    final = ""
    answer.sort()
    for c in range(len(answer)):
        final = final + answer[c]
            
    output.write("Case #{}: {}\n".format(i, final))
    print("Case #{}: {}\n".format(i, final))
    
output.close()
