import os
from sys import argv

class Pancake(object):

    def __init__(self, params):
        params_array = params.split()
        self.cases = params_array[0]
        self.trials = params_array[1:]
        self.answer = []

    def run(self):
        attempt = 1
        for trial in self.trials:
            trial_list = [trial_char for trial_char in trial]
            trial_list.reverse()
            answer = self.get_answer(trial_list)
            self.append_answer(answer, attempt)
            attempt += 1


    def get_answer(self, trial, attempt=0):
        if '-' not in trial:
            return attempt
        trial = self.get_trial_after_flips(trial)
        'flipped'
        return self.get_answer(trial, attempt+1)


    def get_trial_after_flips(self, trial):
        start = 0
        for x in trial:
            if x == '-': 
                location = start
                trial[location] = '+'
                break
            start += 1
        new_start = location
        while True:
            new_start += 1
            if new_start >= len(trial):
                break
            if trial[new_start] == '-':
                trial[new_start] = '+' 
            else:
                trial[new_start] = '-'
        return trial
         
        

    def append_answer(self, answer, attempt):
        self.answer.append('Case #{0}: {1}'.format(attempt, answer))  

    def get_result(self):
        return '\n'.join(self.answer) 

def main(file_name):
    with open(file_name, 'r') as inputs:
        google_input = inputs.read()
    pancake = Pancake(google_input)
    pancake.run()
    answer = pancake.get_result()
    with open('answer.txt', 'wr') as answer_file:
        answer_file.write(answer)


if __name__ == '__main__':
    file_name = argv[1]
    main(file_name)
            
        
