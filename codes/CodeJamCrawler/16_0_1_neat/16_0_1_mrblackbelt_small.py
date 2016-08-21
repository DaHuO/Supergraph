import os
from sys import argv

class Sheep(object):

    def __init__(self, params):
        params_array = params.split()
        self.cases = params_array[0]
        self.trials = params_array[1:]
        self.final_set = set(range(0, 10))
        self.original_set = set()
        self.current_trial = False
        self.answer = []

    def run(self):
        attempt = 1
        for trial in self.trials:
            self.original_set = set()
            trial_num = int(trial)
            answer = self.get_answer(trial_num)
            self.append_answer(answer, attempt)
            attempt += 1


    def get_answer(self, trial, attempt=1):
        if attempt == 1:
            self.current_trial = trial
        if attempt == 1 and trial in [0]:
            return 'INSOMNIA'
        new_list = [int(num) for num in str(trial)] 
        self.original_set.update(new_list)
        if self.original_set == self.final_set:
            return self.current_trial * attempt
        attempt += 1
        return self.get_answer(trial=self.current_trial* attempt, attempt=attempt) 


    def append_answer(self, trial, attempt):
        self.answer.append('Case #{0}: {1}'.format(attempt, trial))  

    def get_result(self):
        return '\n'.join(self.answer) 


if __name__ == '__main__':
    file_name = argv[1]
    with open(file_name, 'r') as inputs:
        google_input = inputs.read()
    sheep = Sheep(google_input)
    sheep.run()
    answer = sheep.get_result()
    with open('answer.txt', 'wr') as answer_file:
        answer_file.write(answer)
            
        
        
        
            

    
