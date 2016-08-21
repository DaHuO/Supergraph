__author__ = 'fbleite'
import timeit

def printOutput (outputSet) :
    for i in range(len(outputSet)):
        textToPrint = ''
        for j in range(len(outputSet[i])):
            textToPrint = textToPrint + ' ' + str(outputSet[i][j])
        print("Case #{}:{}".format(i+1, textToPrint))

#
# sampleOutput = [["Hello", "Bye bye"], ["Its me"]]
# sampleOutput.append(["I'm in California"])
# timeit.timeit(printOutput(sampleOutput))
# timeit.timeit(timeit)