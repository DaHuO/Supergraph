'''
    Author: Thomas Negash
    Date: 4-9-2016

'''

    
class countingSheep:
    def __init__(self, file_name):
        self.file = open(file_name, "r")
        self.checker = [0,1,2,3,4,5,6,7,8,9]
        

    def getList(self, lst):
        ls = []
        for i in range(len(lst)):
            ls.append(int(lst[i]))
        return ls

    def add_num(self, lst, num):
        notFound = True
        for i in range(len(lst)):
            if num == lst[i]:
                notFound = False
        if notFound:
            lst.append(num)

    def addNumber(self, lst, lst2):
        for i in range(len(lst2)):
            self.add_num(lst, lst2[i])
        return lst
                    
    

    def handler(self):
        test_case = int(self.file.readline())
        for i in range(test_case):
            main_list = []
            number = int(self.file.readline())
            o_num = number
            lst = self.getList(list(str(number)))
            lst.sort()
            main_list = self.addNumber(main_list, lst)
            mul = 2
            length = len(main_list)
            insomnia = False
            while len(main_list) < 10:
                number = o_num * mul
                lst = self.getList(list(str(number)))
                lst.sort()
                main_list = self.addNumber(main_list, lst)
                mul += 1
                if (mul >= 20 and len(main_list) == length):
                    insomnia = True
                    break
            if insomnia:
                print("Case #" + str(i+1) + ": " + "INSOMNIA")
            else:
                print("Case #" + str(i+1) + ": " + str(number))
                
                
            
            
                
                    
                
            
















    
