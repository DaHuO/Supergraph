def countingSheep(num):
    if num == 0:
        return 'INSOMNIA'
    a = num
    numbers = set()
    counter = 1
    while len(numbers) != 10:
        for elem in str(a):
            if elem in '0123456789':
                numbers.add(elem)
            
        a += num
        counter += 1
    
    if len(numbers) == 10:
        #print(numbers)
        return a - num
    
def readFile(lines):
    newList = []
    file = open(lines,'r')
    a = file.readlines()[1:]
    for elem in a:
        newList.append(int(elem.strip('\n')))
     
    return newList

def connector(file):
    content = readFile(file)
    counter = 1
    for element in content:
        print('Case #' + str(counter) + ': '+ str(countingSheep(element)))
        counter += 1
    
    return
    
    
