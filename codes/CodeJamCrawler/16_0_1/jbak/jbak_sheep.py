


def main():

    outFile = open('sheep_large.txt', 'w')

    with open('sheepInL.txt','r') as file:
    
        tCases = int(file.readline())
        case = 1
    
        while tCases > 0:
            N = int(file.readline())

            if N == 0:
                message = 'INSOMNIA'

            else:
                seenNum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                notAllSeen = True
                i = 1

                #if not all of the numbers have been seen yet, keep multiplying
                while notAllSeen:
                    newNum = i*N
                    message = str(newNum)

                    for v in message:
                        seenNum[int(v)] = 1

                    i = i+1

                    if 0 not in seenNum:
                        notAllSeen = False


            #print 'Case #' + str(case) + ': ' + message

            outFile.write('Case #' + str(case) + ': ' + message + '\n')

            tCases = tCases - 1
            case = case + 1

    outFile.close()
        

main()