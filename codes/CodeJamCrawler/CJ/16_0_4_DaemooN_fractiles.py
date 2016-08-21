class result_set(object):
    def __init__(self, g_pos, length):
        self.positions_of_g = [g_pos]
        self.length = length
    def iterate(self):
        new_positions = []
        for index in range(self.length):
            if index in self.positions_of_g:
                new_positions+= range(index*self.length, (index*self.length) + self.length)
            else:
                new_positions += [x+(index*self.length) for x in self.positions_of_g]
        self.positions_of_g = new_positions
        self.length = self.length*self.length
    def __str__(self):
        res = []
        for i in range(self.length):
            if i in self.positions_of_g:
                res.append('G')
            else:
                res.append('L')
        return "".join(res)

import math

if __name__=="__main__":
    input_name = "input/4-small.in"
    output_name = "out.tmp"
    file = open(input_name, "r")
    file_out = open(output_name, "w")
    test_cases = int(file.readline())

    for test in range(1, test_cases+1):
        inp = file.readline()[:-1].split(" ")
        #inp = ['3','2','3']
        sets = []

        k = int(inp[0])
        c = int(inp[1])
        s = int(inp[2])
        if k == 1:
            res = "1"

        elif c == 1:
            if s < k:
                res = "IMPOSSIBLE"
            else:
                res = " ".join([str(x+1) for x in range(k)])
        elif s < math.ceil(k/2):
            res = "IMPOSSIBLE"
        else:
            res_list = []
            if k%2 == 0:
                if k/2 > s:
                    res = "IMPOSSIBLE"
                else:
                    for i in range(0, k, 2):
                        res_list.append(str((i+2) + ((i)*k)))
            else:
                if (k+1)/2 > s:
                    res = "IMPOSSIBLE"
                else:
                    for i in range(0, k-1, 2):
                        res_list.append(str((i+2) + ((i)*k)))
                    res_list.append(str(int(k)))

            res = " ".join(res_list)

        print("Case #"+str(test)+": " + str(res))










