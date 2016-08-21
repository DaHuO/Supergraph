
numTestCases=int(raw_input ())

def getindex(self, elem, default):
        try:
            thing_index = self.index(elem)
        except ValueError:
            return default



for x in range (numTestCases):
    i=1
    array=[]
    testCase=int (raw_input())
    while (len(array)<10 and i>0):
        if testCase<1:
            print "Case #"+str(x+1)+": "+"INSOMNIA"
            break;
        else:
            temp=testCase*i
            while temp!=0:
                rem=temp%10
                if (getindex(array,rem,-1) == -1) and len(array)<10:
                    array.append(rem)
                temp=temp/10
        i=i+1
    if testCase>0:
        print "Case #"+str(x+1)+": "+str(testCase*(i-1))

       
            
       

