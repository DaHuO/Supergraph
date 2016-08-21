
import sets

listinput=[]
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in range(0, t):
    n = (raw_input())  # read a list of integers, 2 in this case
    listinput.append(n)
#print list
num=1
#input collected now need to process
for item in listinput:
    listString=list(item)
    length=len(listString)
    count=0
    while(True):
        #find the first - and then reverse everythin till that point
        #print "num="+str(count)
        try:
            index=listString.index("-")
            #print "ind="+str(index)
            while(index<length-1):
                if listString[index+1]=="-":
                    index+=1
                    continue
                else:
                    break
            #print index
            #now reverse the substring and then recheck if there is any
            for ind in range(0,index+1):
                if listString[ind] =="+":
                    listString[ind] = "-"
                elif listString[ind] == "-":
                    listString[ind] = "+"
            count+=1
            #print "".join(listString)
            continue
        except:
            print "case #" + str(num) + ": " + str(count)
            num+=1
            break



