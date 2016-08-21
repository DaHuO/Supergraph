'''
    Author: Thomas Negash
    Date: 4-9-2016

'''
from math import sqrt
from itertools import count, islice
    
class jam:
    def __init__(self, file_name):
        self.file = open(file_name, "r")

    def getNumber(self, lst):
        count = 2
        ls = []
        while count <= 10:
            num = 0
            power = len(lst) - 1
            for i in range(len(lst)):
                if (lst[i] != 0):
                    num += int(lst[i]) * (count**power)
                power -= 1
            if self.isPrime(num):
                return False
            count += 1
            ls.append(num)
        return ls

    def isPrime(self, num):
        return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num)-1)))                

    def getDiv(self, lst):
        ls = []
        for j in range(len(lst)):
            for i in range(2, lst[j]//2):
                if (lst[j] % i == 0):
                    ls.append(str(i))
                    break
        return ls

    def addNum(self, num, N):
        while self.isPrime(num):
            if num < (2**N) -1:
                num += 2
                
        return num
                

    def handler(self):
        test_case = int(self.file.readline())
        for i in range(test_case):
            lst = self.file.readline().split(" ")
            N = int(lst[0])
            J = int(lst[1])
            ls = ""
            for j in range(N):
                if j == 0 or j == N-1:
                    ls += "1"
                else:
                    ls += "0"
            num = int(ls, 2)
            count = 0
            print("Case #" + str(i+1) + ":")
            while count < J:
                if self.isPrime(num):
                    num = self.addNum(num, N)
                n = "{0:b}".format(num)
                lst = self.getNumber(list(n))
                if not lst:
                    num = self.addNum(num+2,N)
 
                else:
                    print("{0:b}".format(num) + " " + " ".join(self.getDiv(lst)))
                    count += 1
                    num = self.addNum(num+2, N)

            

