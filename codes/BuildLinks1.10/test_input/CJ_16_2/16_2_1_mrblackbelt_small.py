import os
from sys import argv

class LastWord(object):
    zero = ['z', 'e', 'r', 'o']
    one = ['o', 'n', 'e']
    two = ['t', 'w', 'o']
    three = ['t', 'h', 'r', 'e', 'e']
    four = ['f', 'o', 'u', 'r']
    five = ['f', 'i', 'v', 'e']
    six = ['s', 'i', 'x']
    seven = ['s', 'e', 'v', 'e', 'n']
    eight = ['e', 'i', 'g', 'h', 't']
    nine = ['n', 'i', 'n', 'e']
    

    def __init__(self, params):
        params_array = params.split()
        self.cases = params_array[0]
        self.trials = params_array[1:]
        self.answer = []

    def run(self):
        attempt = 1
        for trial in self.trials:
            numbers = self.get_list_numbers_from_trial(trial.lower(), list())
            answer = ''.join(numbers)
            self.append_answer(answer, attempt)
            attempt += 1


    def get_list_numbers_from_trial(self, trial, numbers=list()):
        print trial
        print 'z' in trial
        if 'z' in trial:
            numbers.append('0')
            for letter in self.zero:
                trial = trial.replace(letter, '', 1)
            return self.get_list_numbers_from_trial(trial, numbers)
        if 'w' in trial:
            numbers.append('2')
            for letter in self.two:
                trial = trial.replace(letter, '', 1)
            return self.get_list_numbers_from_trial(trial, numbers)
        if 'u' in trial:
            numbers.append('4')
            for letter in self.four:
                trial = trial.replace(letter, '', 1)
            return self.get_list_numbers_from_trial(trial, numbers)
        if 'x' in trial:
            numbers.append('6')
            for letter in self.six:
                trial = trial.replace(letter, '', 1)
            return self.get_list_numbers_from_trial(trial, numbers)
        if 'g' in trial:
            numbers.append('8')
            for letter in self.eight:
                trial = trial.replace(letter, '', 1)
            return self.get_list_numbers_from_trial(trial, numbers)
        if 'v' in trial and 'f' in trial:
            numbers.append('5')
            for letter in self.five:
                trial = trial.replace(letter, '', 1)
            return self.get_list_numbers_from_trial(trial, numbers)
        if 'v' in trial and 's' in trial:
            numbers.append('7')
            for letter in self.seven:
                trial = trial.replace(letter, '', 1)
            return self.get_list_numbers_from_trial(trial, numbers)
        if 'o' in trial and 'n' in trial:
            numbers.append('1')
            for letter in self.one:
                trial = trial.replace(letter, '', 1)
            return self.get_list_numbers_from_trial(trial, numbers)
        if 't' in trial and 'h' in trial:
            numbers.append('3')
            for letter in self.three:
                trial = trial.replace(letter, '', 1)
            return self.get_list_numbers_from_trial(trial, numbers)
        if trial:   
            numbers.append('9')
            for letter in self.nine:
                trial = trial.replace(letter, '', 1)
            return self.get_list_numbers_from_trial(trial, numbers)
        return sorted(numbers)


    def append_answer(self, answer, attempt):
        self.answer.append('Case #{0}: {1}'.format(attempt, answer))  

    def get_result(self):
        return '\n'.join(self.answer) 

def main(file_name):
    with open(file_name, 'r') as inputs:
        google_input = inputs.read()
    last_word = LastWord(google_input)
    last_word.run()
    answer = last_word.get_result()
    with open('answer.txt', 'wr') as answer_file:
        answer_file.write(answer)


if __name__ == '__main__':
    file_name = argv[1]
    main(file_name)
            
        
