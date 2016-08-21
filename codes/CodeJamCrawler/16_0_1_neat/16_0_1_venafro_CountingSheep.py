SET = [0,1,2,3,4,5,6,7,8,9]


def get_number(n):
    return list(set(list(str(n))))


def calculate(input):
    iterations = 2
    SET = [0,1,2,3,4,5,6,7,8,9]
    
    for i in get_number(int(input)):
        try: SET.remove(int(i))
        except: a = 9
    

    if len(SET) == 0: return input
            
    while(iterations<101):
        n = iterations*input

        for i in get_number(int(n)):
         try: SET.remove(int(i))
         except: a = 9
        if len(SET) == 0: return n
        iterations=iterations+1
    
    if iterations>100: return "INSOMNIA"    


file = open('A-large0.in','r')
total = int(file.readline())
for i in range(1,total+1):
    v1,v2=[],[]
    
    input = file.readline()

    output = calculate(int(input))

    try:
       b=output+1     
       print 'case #%d: %d' % (i,output)
    except:
       print 'case #%d: %s' % (i,output) 
