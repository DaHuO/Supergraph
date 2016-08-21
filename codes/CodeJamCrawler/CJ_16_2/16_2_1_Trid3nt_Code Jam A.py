boo = 0
answers = []

count = 0


nums = []
with open('alarge.txt', 'r') as fi:
    for line in fi:
        if boo == 0:
            boo = 1
            continue
        
        count += 1
        vals = str(line.split()[0])
        #print vals, count

        almostanswer = [0] * 10
        if vals.count('Z') > 0:
            temp = vals.count('Z')
            almostanswer[0] = temp

            vals = vals.replace("Z","",temp)
            vals = vals.replace("E","",temp)
            vals = vals.replace("R","",temp)
            vals = vals.replace("O","",temp)

        if vals.count('X') > 0:
            temp = vals.count('X')
            almostanswer[6] = temp

            vals = vals.replace("S","",temp)
            vals = vals.replace("I","",temp)
            vals = vals.replace("X","",temp)
                
        if vals.count('G') > 0:
            temp = vals.count('G')
            almostanswer[8] = temp

            vals = vals.replace("E","",temp)
            vals = vals.replace("I","",temp)
            vals = vals.replace("G","",temp)
            vals = vals.replace("H","",temp)
            vals = vals.replace("T","",temp)

        if vals.count('W') > 0:
            temp = vals.count('W')
            almostanswer[2] = temp

            vals = vals.replace("T","",temp)
            vals = vals.replace("W","",temp)
            vals = vals.replace("O","",temp)

        if vals.count('H') > 0:
            temp = vals.count('H')
            almostanswer[3] = temp

            vals = vals.replace("T","",temp)
            vals = vals.replace("H","",temp)
            vals = vals.replace("R","",temp)
            vals = vals.replace("E","",temp)
            vals = vals.replace("E","",temp)

        if vals.count('R') > 0:
            temp = vals.count('R')
            almostanswer[4] = temp

            vals = vals.replace("F","",temp)
            vals = vals.replace("O","",temp)
            vals = vals.replace("U","",temp)
            vals = vals.replace("R","",temp)

        if vals.count('O') > 0:
            temp = vals.count('O')
            almostanswer[1] = temp

            vals = vals.replace("O","",temp)
            vals = vals.replace("N","",temp)
            vals = vals.replace("E","",temp)

        if vals.count('F') > 0:
            temp = vals.count('F')
            almostanswer[5] = temp

            vals = vals.replace("F","",temp)
            vals = vals.replace("I","",temp)
            vals = vals.replace("V","",temp)
            vals = vals.replace("E","",temp)

        if vals.count('V') > 0:
            temp = vals.count('V')
            almostanswer[7] = temp

            vals = vals.replace("S","",temp)
            vals = vals.replace("E","",temp)
            vals = vals.replace("V","",temp)
            vals = vals.replace("E","",temp)
            vals = vals.replace("N","",temp)

        if vals.count('I') > 0:
            temp = vals.count('I')
            almostanswer[9] = temp

            vals = vals.replace("N","",temp)
            vals = vals.replace("I","",temp)
            vals = vals.replace("N","",temp)
            vals = vals.replace("E","",temp)

        ans = ""
        for i in range(len(almostanswer)):
            ans = ans + almostanswer[i]*str(i)

        answers.append(ans)
    fi.close

val = 1
with open('alargeout.txt', 'a') as fi:
    for answer in answers:
        fi.write('Case #' + str(val) + ': ' + str(answer) + '\n')
        val += 1
    fi.close
