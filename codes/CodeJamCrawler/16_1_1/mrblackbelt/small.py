import os
from sys import argv

class LastWord(object):

    def __init__(self, params):
        params_array = params.split()
        self.cases = params_array[0]
        self.trials = params_array[1:]
        self.answer = []

    def run(self):
        attempt = 1
        for trial in self.trials:
            original_trial_list = [trial_char for trial_char in trial]
            sorted_trial_list = sorted(original_trial_list)
            biggest_letter = sorted_trial_list[-1] 
            answer = self.get_word(original_trial_list, biggest_letter)
            self.append_answer(answer, attempt, biggest_letter)
            attempt += 1

    def get_word(self, original_trial_list, biggest_letter):
        final_word = ''
        final = False
        for word in original_trial_list:
            current_letters = [char for char in final_word]
            if word == biggest_letter:
                final_word = '{0}{1}'.format(word, final_word)
            elif final_word and word >= max(current_letters):
                final_word = '{0}{1}'.format(word, final_word)
            else:
                final_word = '{0}{1}'.format(final_word, word)
        return final_word
            
    
    def append_answer(self, answer, attempt, biggest_letter):
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
            
        
