'''
    Author: Thomas Negash
    Date: 4-9-2016

'''

class revengePancakes:
    def __init__(self, file_name):
        self.file = open(file_name, "r")

    def handler(self):
        test_case = int(self.file.readline())
        for i in range(test_case):
            lst = list(self.file.readline())
            self.checkNull(lst)
            flips = self.getFlips(lst)
            print("Case #" + str(i+1) + ": " + str(flips))

    def checkNull(self, lst):
        null = False
        for i in range(len(lst)):
            if (lst[i] == "\n"):
                null = True
        if null:
            lst.pop()
                

    def getFlips(self, lst):
        flips = 0
        while (self.notDone(lst)):
            count = 1
            first = lst[0]
            for i in range(1, len(lst)):
                if (lst[i] != lst[0]):
                    break
                count += 1
            lst = self.flip(lst, count)
            flips += 1
        return flips
            
    def flip(self, lst, stop):
        ls = []
        for i in range(stop):
            ls.append("+" if lst[i] == "-" else "-")
        if (stop < len(lst)):
            for j in range(stop, len(lst)):
                ls.append(lst[j])
          #  ls.extend(lst[stop:-1])
        return ls

    def notDone(self, lst):
        for i in range(len(lst)):
            if (lst[i] == "-"):
                return True
        return False
                
                
                
            
            
            
                
                
            
            
                
                    
                
            
















    
