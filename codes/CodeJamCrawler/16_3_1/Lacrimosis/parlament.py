import time

start_time = time.time()

inputFile = open("A-large (1).in", 'r')
outputFile = open("parlaimentOut.txt", 'w')

num_of_testcases = int(inputFile.readline())
print("Num of tcs: ", str(num_of_testcases))

num_of_parties = 0
parties_men = list()



for testcase in range(num_of_testcases):
    num_of_parties = int(inputFile.readline().strip())
    parties_men = inputFile.readline().strip().split()
    dictionary = dict()
    for p in range(num_of_parties):
        character = str(chr(65 + p))
        dictionary[character] = int(parties_men[p])

    whole_out = ""
    najwieksza = 'A'
    while True:
        lacznie = sum(dictionary.values())
        if lacznie < 1:
            break

        para = ""

        najwieksza = max(dictionary, key=dictionary.get)
        dictionary[najwieksza] -= 1
        para = para + najwieksza;

        if lacznie == 3:
            whole_out += para+" "
            continue

        if (sum(dictionary.values()) == 0): break

        najwieksza = max(dictionary, key=dictionary.get)
        dictionary[najwieksza] -= 1
        para = para + najwieksza;

        whole_out += para + " "

    print('Case #'+ str(testcase + 1) + ": " + whole_out.rstrip())
    outputFile.write('Case #'+ str(testcase + 1) + ": " + whole_out.rstrip()+'\n')

inputFile.close()
outputFile.close()

print("--- %s seconds ---" % (time.time() - start_time))
