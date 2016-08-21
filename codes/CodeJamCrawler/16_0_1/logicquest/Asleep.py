class Asleep:
    
    def __init__(self):
        self.list_numbers = [None]*10
        self.count=0
        self.i=1
        self.current_val=0

    def store_digits(self,n):
        while n != 0:
            first_num = n %10
            if not self.list_numbers[first_num]:
                self.count+=1
                self.list_numbers[first_num]=1
            n= n / 10            
            
    def fall_asleep(self,n):
        if n == 0:
            return "INSOMNIA"
        else:
            while self.count != 10:
                self.current_val=n*self.i
                self.store_digits(self.current_val)
                self.i+=1
            return self.current_val
            
# user_input = raw_input("")
# for i in range(len(user_input)):
#     a = Asleep()
#     n= raw_input("")
#     print str(a.fall_asleep(n))     
# a = Asleep()
# # print str()
# a.fall_asleep(2)

with open("A-large.in") as f:
    out_list=[]
    content = f.readlines()
    for i in range(1,len(content)):
        inp = int(content[i])
        a = Asleep()
        print "Case #"+str(i) +": "+ str(a.fall_asleep(inp))
