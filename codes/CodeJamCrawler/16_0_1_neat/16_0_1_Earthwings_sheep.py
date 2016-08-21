'''
Created on 09.04.2016

@author: Dennis Nienhüser <nienhueser@kde.org>
'''

import argparse

def lastNumber(number):
    seen = []
    for i in range(1, 1000):
        value = str(i*number)
        for character in value:
            if character not in seen:
                seen.append(character)
                if len(seen) == 10:
                    return value

    return 'INSOMNIA'

def parse(filename):
    with open(filename) as file:
        numbers = file.readlines()
    numbers = [int(i) for i in numbers]
    return numbers[1:] if len(numbers) > 0 else []

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Code Jam 2016 Q1: Counting Sheep')
    parser.add_argument('file', help='Input text file')
    args = parser.parse_args()
    input = parse(args.file)
    for index, number in enumerate(input):
        print('Case #{}: {}'.format(index+1, lastNumber(number)))
    