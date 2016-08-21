import logging
import numpy as np

def countingSheep(filename='inputA.in'):
    #reader
    rownum = 0
    numbers = list()
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
    

def pancakes(filename='inputB.in'):
    #reader
    rownum = 0
    stacks = list()
    with open('Input/' + filename, 'rb') as file:
        for row in file:
            if rownum > 0:
                stack = list()
                for e in row.strip():
                    if e == '+':
                        stack.append(1)
                    else: # e == '-'
                        stack.append(-1)
                stacks.append(stack)
            rownum += 1
    logging.debug('List of stacks: ' + str(stacks))

    #algo
    solList = list()
    for stack in stacks:
        n = 0
        while True:
            logging.debug('n: ' + str(n))
            logging.debug('Stack: ' + str(stack))
            while stack and stack[-1]==1:
                stack = stack[0:-1]
            if not stack:
                break
            logging.debug('Stack after pruning: ' + str(stack))
            if stack[0] == -1:
                stack = [ e * -1 for e in list(reversed(stack))]
            else:
                # TODO: mehrere umdrehen wenn es sich anbietet!
                i = 0
                while stack[i] == 1:
                    stack[i] = -1
                    i += 1
            n += 1
            logging.debug('Stack after operation: ' + str(stack))
        solList.append(n)
        logging.debug('Final n: ' + str(n))

    #writer
    with open('Output/' + filename.split('.')[0] + '.out', 'w') as file:
        for i in range(len(solList)):
            file.write('Case #' + str(i+1) + ': ' + str(solList[i]) + '\n')



if __name__ == "__main__":

    FORMAT = '%(levelname)s: %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

    # countingSheep('inputLargeA.in')
    pancakes('inputLargeB.in')













