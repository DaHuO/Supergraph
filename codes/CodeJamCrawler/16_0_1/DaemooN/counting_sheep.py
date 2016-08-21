class sheepcounter(object):
    seen_numbers = ()
    def __init__(self, number):
        self.number = number
        self.seen_numbers = set(str(number))
        self.number_of_iterations = 0
        self.iteration = 2
    def iterate(self):
        if self.number_of_iterations > 500:
            return "INSOMNIA"
        self.seen_numbers.update(set(str(self.number * self.iteration)))
        self.number_of_iterations += 1
        self.iteration+= 1
        if len(self.seen_numbers) == 10:
            return self.number * (self.iteration - 1)
        else:
            return None

if __name__=="__main__":
    input_name = "input/1-small.in"
    output_name = "out.tmp"
    file = open(input_name, "r")
    file_out = open(output_name, "w")
    test_cases = int(file.readline())
    for test in range(0, test_cases):
        inp = int(file.readline())
        res = None
        counter = sheepcounter(inp)
        while res == None:
            res = counter.iterate()
        print("Case #" + str(test + 1) +": "+ str(res))
