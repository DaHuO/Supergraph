file = open('B-large (1).in')
lines = file.readlines()

t = int(lines[0])
def last_index(l, value):
    for i, v in enumerate(reversed(l)):
        if v == value:
            return len(l) - 1 - i
    return -1
    
def done(stack):
    for pancake in stack:
        if pancake == '-':
            return False
    return True


def flip(stack, height):
    top = stack[:height]
    bottom = stack[height:]
    top = list(top)
    for i in range(0, height):
        top[i] = ('+' if top[i] == '-' else '-')
    top.reverse()
    return ''.join(top) + bottom


for memes in range(0, int(t)):
    flips = 0
    pancake = lines[1 + memes]
    stack = pancake
    while not done(stack):
        if stack[0] == '+':
            stack = flip(stack, stack.index('-'))
        else:
            stack = flip(stack, last_index(stack, '-') + 1)
        flips += 1
    print('Case #{}: {}'.format(memes+1, flips))




    
    '''
    var = 0
    flipped = 0
    
    pancake = lines[1 + i]
    pancake = pancake.strip()
    strPancake = pancake
    pancake = list(pancake)
    revPancake = pancake[::-1]
    for x in range(0, len(strPancake)):
        print(strPancake)
        flipped += 1
        indexer = -1 
        strPancake = pancake
        strPancake = ''.join(strPancake)
        strPancake = re.sub(r'(\++)$', '',strPancake)
        strPancake = list(strPancake)
        strPancake = strPancake[::-1]
        #print(strPancake)
        strPancake = [ch.replace('-', 'x') for ch in strPancake]
        strPancake = [ch.replace('+', '-') for ch in strPancake]
        strPancake = [ch.replace('x', '+') for ch in strPancake]
        #now you REPLACE
        strPancake = ''.join(strPancake)
        
        strPancake = re.sub(r'^(\++)', lambda m: len(m.group(1)) * '-', strPancake)
        
        strPancake = (strPancake[0:strPancake.index("-")])[::-1]            
        print(strPancake)
    print('Case #{}: {} {}'.format(i+1, strPancake, flipped))
    
''''''
for i in range(0, int(t)):
    var = 0
    flipped = 0
    
    pancake = lines[1 + i]
    pancake = pancake.strip()

    pancake = list(pancake)
    revPancake = pancake[::-1]
    
    for x in range(0, len(pancake)):
        indexer = -1
        if pancake[x] == "-":
                   
            if x == 0:
                pancake[x] = "+"
                flipped += 1
           # elif (not((x + 1 > len(pancake)) and (pancake[x+1] == '-'))):
           #     print("REVERSED")
            #    pancake[0:x] = (pancake[0:x])[::-1]
            #    flipped += 1
            
                 
            #elif pancake[x+1] == 
            else:
                #reverse everything up to x, and swap the signs
     
                pancake[0:x] = (pancake[0:x])[::-1]
                flipped += 1
                for gg in pancake[0:x]:
                    
                    indexer += 1
                    if gg == "-":
                        pancake[indexer] = "+"
                    else:
                        pancake[indexer] = "-" 
                        

   # print(pancake)
 

            
    print('Case #{}: {} {}'.format(i+1, pancake, flipped))
        

   '''

