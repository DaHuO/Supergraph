import logging
import numpy as np


def standingOvations(filename='inputA.in'):
    rownum = 0
    solList = list()
    # reader
    with open('Input/' + filename, 'rb') as file:
        for row in file:
            if rownum > 0:
                s = row.split(' ')[1].strip()
                y = calcAudience(s)
                logging.debug('Input: ' + s + '\tOutput: ' + str(y))
                solList.append(str(y))
            rownum += 1
    # writer
    with open('Output/' + filename.split('.')[0] + '.out', 'w') as file:
        for i in range(len(solList)):
            file.write('Case #' + str(i+1) + ': ' + solList[i] + '\n')


def countingSheep(filename='inputA.in'):
    #reader
    rownum = 0
    numbers = list()
    # reader
    with open('Input/' + filename, 'rb') as file:
        for row in file:
            if rownum > 0:
                numbers.append(int(row))
            rownum += 1
    logging.debug('List of numbers: ' + str(numbers))
    
    #algo
    solList = list()
    for e in numbers:
        if e == 0:
            solList.append('INSOMNIA')
            continue
        currentNumber = e
        check = [0,1,2,3,4,5,6,7,8,9]
        while check:
            logging.debug('BEFORE: Current number: ' + str(currentNumber) + '\tChecklist: ' + str(check))
            digits = [int(x) for x in str(currentNumber)]
            removables = list()
            for f in check:
                if f in digits:
                    removables.append(f)
            for f in removables:
                check.remove(f)
            logging.debug('AFTER: Current number: ' + str(currentNumber) + '\tChecklist: ' + str(check))
            currentNumber += e
        solList.append(str(currentNumber-e))

    #writer
    with open('Output/' + filename.split('.')[0] + '.out', 'w') as file:
        for i in range(len(solList)):
            file.write('Case #' + str(i+1) + ': ' + solList[i] + '\n')
    

if __name__ == "__main__":

    FORMAT = '%(levelname)s: %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

    countingSheep('inputLargeA.in')













