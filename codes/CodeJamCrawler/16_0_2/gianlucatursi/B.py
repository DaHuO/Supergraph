array = []
with open('input_small.txt','r') as reader :
    for line in reader :
        array.append(line)


for case in range(1, int(array[0])+1):

    string = array[case]

    if len(string) == 1 and string == "+":
        print "Case #" + str(case) + ": 0"
    elif len(string) == 1:
        print "Case #" + str(case) + ": 1"
    elif string.count("+") == len(string)-1:
        print "Case #" + str(case) + ": 0"
    elif len(string) > 1:

        tmp = string[0]
        newTop = tmp
        endReplace = 0
        step = 0
        for i in string[1:]:
            if string.count("+") != len(string)-1:
                if tmp == i:
                    endReplace += 1
                    newTop += tmp
                else:
                    if newTop.find("-") == -1:
                        newTop = newTop.replace("+","-")
                    else:
                        newTop = newTop.replace("-","+")

                    string = newTop + string[endReplace+1:]

                step += 1

        print "Case #" + str(case) + ": " + str(step)
