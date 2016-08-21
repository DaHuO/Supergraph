import math

class FileHandling:  # class which handles file operation

    def __init__(self,filename='input.txt'):
        """
        constructor for class
        :param filename: File's absolute path where you want to store the output
        :return: None
        """
        self.filename = filename
        self.fw = open(filename, "r+")


    def log_msg(self, msg):
        """
        logs message in file
        :param msg: string to log in file
        :return: none
        """
        # self.fw.write("Tic-Tac-Toe tournament between " + p1name + "(X) and " + p2name + "(O):\n")
        self.fw.write(msg + "\n")

    def read(self):
        return self.fw.readline()

    def __del__(self):
        self.fw.close()



f = FileHandling()
_size = int(f.read())
for i in range(_size):
    num = int(f.read())
    mul = 1
    f_l = [0 for x in range(10)]
    ans = 0
    while f_l.count(0) != 0:
        n = num * mul
        if n == 0:
            ans = "INSOMNIA"
            break
        else:
            ans = n
        #print("num:",n)
        while n:
            digit = n % 10
            # do whatever with digit
            f_l[digit] = 1
            # remove last digit from number (as integer)
            n //= 10
        mul += 1
    print("Case #{}:".format(i+1),ans)