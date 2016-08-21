import sys

class CountingSheep:
    last_number_seen = 0
    result = ""    
        
    def __init__(self):
        self.last_number_seen = 0
            
    def solve(self, chosen_number):
         if (int(chosen_number) == 0):
            self.result = "INSOMNIA"
         else:
            self.result = self.get_last_number_seen(chosen_number)

    def get_last_number_seen(self, chosen_number):
        seen_all_numbers = False
        iterations = 1
        numbers_seen = []
        
        while (seen_all_numbers == False):
            self.last_number_seen = iterations * int(chosen_number)
            for number in str(self.last_number_seen):
                if ((int(number) in numbers_seen) == False):
                    numbers_seen.append(int(number))
            
            seen_all_numbers = self.verify_numbers_seen(numbers_seen)
                                                        
            iterations += 1;
        
        return self.last_number_seen

    def verify_numbers_seen(self, numbers_seen):
        return len(numbers_seen) == 10
                                  
file = sys.stdin
#file = open('A-small-practice.in', "r")
counter = 1
line = file.readline()
line = file.readline()
while line:    
    chosen_number = line    
    counting_sheep = CountingSheep()    
    counting_sheep.solve(chosen_number)
    
    print "Case #{}: {}".format(counter, counting_sheep.result)
    line = file.readline()    
    counter += 1