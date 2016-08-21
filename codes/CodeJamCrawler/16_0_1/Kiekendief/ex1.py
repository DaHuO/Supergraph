from sets import Set

#f = open("input1.txt","r")
#f = open("A-small-attempt0.in","r")
f = open("A-large.in","r")

g = open ("output.log","w")

def get_digits_from_number(number):
    #print "Check %s"%number
    number_str = str(number)
    result = Set()
    for c in number_str:
        result.add(c)
    return result
    
def get_last_number(number):
    if number == 0:
        return None
    count = 1
    digits = Set()
    
    while len(digits)<10:
        digits |= get_digits_from_number(count*number)
        count += 1
        #print digits

    return (count-1)*number

runs = int(f.readline())

for i in range(runs) :
    number = int(f.readline())
    result = get_last_number(number)
    if result:
        line = "Case #%d: %d"%(i+1,result)
        print line
        g.write(line+'\n')
    else :
        line ="Case #%d: INSOMNIA"%(i+1)
        print line
        g.write(line+'\n')

f.close()
g.close()