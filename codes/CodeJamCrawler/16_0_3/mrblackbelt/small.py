import os
from sys import argv
import helpers

class Jamcoin(object):

    def __init__(self, params):
        params_array = params.split()
        self.cases = params_array[0]
        jamcoin_length = int(params_array[1])
        self.jamcoin_answers = int(params_array[2])
        self.potential_jamcoins = helpers.generate_possible_jamcoins(int(jamcoin_length))
        self.answer = []

    def run(self):
        attempt = 1
        while True: 
            print len(self.answer), 'length of answer', self.jamcoin_answers
            for potential_jamcoin in self.potential_jamcoins:
                if len(self.answer) >= self.jamcoin_answers:
                    return False 
                print potential_jamcoin
                jamcoin_bases = self.get_bases_for_jamcoin(int(potential_jamcoin))
                if self.jamcoin_has_prime_base(jamcoin_bases):
                    print jamcoin_bases, 'prime base'
                    continue 
                print 'not prime'
                divisors_list = self.get_base_divisors(jamcoin_bases) 
                print divisors_list
                divisors_string = ' '.join(str(divisor) for divisor in divisors_list)
                print divisors_string
                self.append_answer(attempt, potential_jamcoin, divisors_string) 
                attempt += 1
    
    def get_base_divisors(self, jamcoin_bases):
        divisors_list = []
        for jamcoin_base in jamcoin_bases:
            divisor = helpers.get_first_divisor(jamcoin_base) 
            divisors_list.append(divisor)
        return divisors_list

    def jamcoin_has_prime_base(self, jamcoin_bases):
        print jamcoin_bases
        return [base for base in jamcoin_bases if helpers.is_prime(base)]
        
    def get_bases_for_jamcoin(self, potential_jamcoin):
        start = 2
        end = 10
        jamcoin_bases = []
        while start <= end:
            jamcoin_bases.append(helpers.number_to_base(potential_jamcoin, start))
            start += 1
        return jamcoin_bases
        
    def append_answer(self, attempt, jamcoin, base_divisors):
        self.answer.append('{1} {2}'.format(attempt, jamcoin, base_divisors))  

    def get_result(self):
        str1 = 'Case #1:\n'
        str2 = '\n'.join(self.answer) 
        return '{0}{1}'.format(str1, str2)

def main(file_name):
    with open(file_name, 'r') as inputs:
        google_input = inputs.read()
    jamcoin = Jamcoin(google_input)
    jamcoin.run()
    answer = jamcoin.get_result()
    with open('answer.txt', 'wr') as answer_file:
        answer_file.write(answer)



if __name__ == '__main__':
    file_name = argv[1]
    main(file_name)
            
        
