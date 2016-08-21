from abc import ABCMeta, abstractmethod
import math

class InputFileReader(object):
	def __init__(self, filename):
		self.input_file = open(filename + '.in', 'r')
	
	def read_int(self):
		return int(self.read_string())

	def read_int_list(self, separator):
		number_strings = self.read_string_list(separator)
		return [int(item) for item in number_strings]

	def read_float_list(self, separator):  
		number_strings = self.read_string_list(separator)
		return [float(item) for item in number_strings]  

	def read_string_list(self, separator):
		line = self.read_string()
		string_tuple = tuple((line.split(separator)))
		return string_tuple

	def read_string(self):
		line = self.input_file.readline()
		if ('\n' == line[-1]):
			line = line[:-1]
		return line
		
class OutputFileWriter(object):
	def __init__(self, filename):
		self.output_file = open(filename + '.out', 'w')
		self.case_num = 1
		
	def write(self, string_list):
		for out_string in string_list:
			self.output_file.write('Case #%d: %s\n' % (self.case_num, out_string))
			self.case_num += 1
			
	
class Problem(object):
	__metaclass__ = ABCMeta
	
	def __init__(self, filename):
		self.input_reader = InputFileReader(filename)
		self.output_writer = OutputFileWriter(filename)
		self.results = []
		self.initialize_from_input()
		
	@abstractmethod
	def initialize_from_input(self):
		pass
		
	@abstractmethod
	def solve_case(self):
		pass
		
	def solve(self):
		for i in xrange(self.number_of_cases):
			self.solve_case()
		self.output_writer.write(self.results)

		
class CommonProblem(Problem):
	__metaclass__ = ABCMeta
		
	def initialize_from_input(self):
		self.number_of_cases = self.input_reader.read_int()
		
def get_divisor(number):
    for i in xrange(2, 1+int(math.sqrt(number))):
        if (0 == number%i):
            return i
    return -1

def check_number_string(number_string):
    result = []
    for base in xrange(2,11):
        divisor = get_divisor(int(number_string, base))
        if (-1 == divisor):
            return None
        else:
            result.append(str(divisor))
    result =  " ".join(result)
    return result

def solve(K, C, S):
    if (S*C < K):
        return "IMPOSSIBLE"
    result = []
    current_digit = K
    done = False
    while not done:
        index = 1
        for level in xrange(0,C):
            index += (current_digit-1) * (K**level)
            if (1 < current_digit):
                current_digit -= 1
            else:
                done = True
        result.append(str(index))
    return " ".join(result)


class CurrentProblem(CommonProblem):
	def solve_case(self):
		l = self.input_reader.read_int_list(" ")
		K = l[0]
		C = l[1]
		S = l[2]
		self.results.append(solve(K,C,S))
		
if "__main__" == __name__:
        filename = "D-large"
	current_problem = CurrentProblem(filename)
	current_problem.solve()
