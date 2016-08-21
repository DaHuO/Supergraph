from collections import OrderedDict
from operator import itemgetter

from base import GoogleJamBaseClass


class A(GoogleJamBaseClass):
    def read_case(self, input_file):
        input_file.readline()
        return input_file.readline().rstrip('\n').split(' ')

    def solve(self, case):
        letters_counts = []
        total_count = 0
        alphabet = list(map(chr, range(97, 123)))
        for idx, letter in enumerate(alphabet):
            if idx == len(case):
                break
            number = int(case[idx])
            total_count += number
            letters_counts.append((letter, number))
        plan = []
        while len(letters_counts) > 0:
            letters_counts = sorted(letters_counts, key=itemgetter(1), reverse=True)
            new_letters = []
            if letters_counts[0][1] > letters_counts[1][1]:
                plan.append(letters_counts[0][0])
                new_letters.append((letters_counts[0][0], int(letters_counts[0][1]) - 1))
                for i in range(1, len(letters_counts)):
                    new_letters.append((letters_counts[i][0], int(letters_counts[i][1])))
            else:
                if len(letters_counts) > 2:
                    if letters_counts[2][1] == letters_counts[1][1]:
                        plan.append(letters_counts[0][0])
                        if int(letters_counts[0][1]) > 1:
                            new_letters.append((letters_counts[0][0], int(letters_counts[0][1]) - 1))
                        for i in range(1, len(letters_counts)):
                            new_letters.append((letters_counts[i][0], int(letters_counts[i][1])))
                    else:
                        plan.append(letters_counts[0][0] + letters_counts[1][0])
                        if letters_counts[0][1] > 1:
                            new_letters.append((letters_counts[0][0], int(letters_counts[0][1]) - 1))
                        if letters_counts[1][1] > 1:
                            new_letters.append((letters_counts[1][0], int(letters_counts[1][1]) - 1))
                        for i in range(2, len(letters_counts)):
                            new_letters.append((letters_counts[i][0], int(letters_counts[i][1])))
                else:
                    plan.append(letters_counts[0][0] + letters_counts[1][0])
                    if letters_counts[0][1] > 1:
                        new_letters.append((letters_counts[0][0], int(letters_counts[0][1]) - 1))
                    if letters_counts[1][1] > 1:
                        new_letters.append((letters_counts[1][0], int(letters_counts[1][1]) - 1))
                    for i in range(2, len(letters_counts)):
                        new_letters.append((letters_counts[i][0], int(letters_counts[i][1])))
            letters_counts = new_letters
        return ' '.join(plan)


A().run('A-large (1).in')
