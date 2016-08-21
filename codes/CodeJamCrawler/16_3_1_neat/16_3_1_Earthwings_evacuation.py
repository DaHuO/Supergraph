'''
Created on 08.05.2016

@author: Dennis Nienhüser <nienhueser@kde.org>
'''

import argparse

def toChar(number):
    return chr(ord('A') + number)

def plan(number):
    
    plan = ''
    while sum(number) > 0:
        maxCount = max(number)
        person = number.index(maxCount)
        parties = sum([1 for i in number if i > 0])
        if parties == 2 and sum(number) > 1:
            res = ' '
            for idx, value in enumerate(number):
                if value > 0:
                    number[idx] = number[idx] - 1
                    res += toChar(idx)
            plan += res 
        else:
            plan += ' {}'.format(toChar(person))
            number[person] = number[person]-1
    return plan.strip()

def parse(filename):
    with open(filename) as file:
        numbers = file.readlines()
    numbers = numbers[1:]
    result = []
    for i in range(len(numbers)):
        if i % 2 == 1:
            values = numbers[i].split(' ')
            result.append([int(i) for i in values])
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Code Jam 2016 Q1: Counting Sheep')
    parser.add_argument('file', help='Input text file')
    args = parser.parse_args()
    problem = parse(args.file)
    for index, number in enumerate(problem):
        print('Case #{}: {}'.format(index+1, plan(number)))
    