g = open("digits_out.txt","w").close()
f = open("digits_in.txt","r")
g = open("digits_out.txt","a")
linecount = int(f.readline())
linenum = 0
for line in f:
    linenum+=1
    myArray = []
    if ('\n') in line:
        line = line.replace('\n','')
    temp = list(line)
    for letter in line:
        
        if(letter=='Z'):
            myArray.append(0)
            temp.remove('Z')
            temp.remove('E')
            temp.remove('R')
            temp.remove('O')
            
    line = ''.join(temp)
    temp = list(line)
    for letter in line:
        
        if(letter=='W'):
            myArray.append(2)
            temp.remove('T')
            temp.remove('W')
            temp.remove('O')
            
    line = ''.join(temp)
    for letter in line:
        
        if(letter=='U'):
            myArray.append(4)
            temp.remove('F')
            temp.remove('O')
            temp.remove('U')
            temp.remove('R')
            
    line = ''.join(temp)
    
    for letter in line:
        
        if(letter=='X'):
            myArray.append(6)
            temp.remove('S')
            temp.remove('I')
            temp.remove('X')
            
            
    line = ''.join(temp)
    for letter in line:
        
        if(letter=='G'):
            myArray.append(8)
            temp.remove('E')
            temp.remove('I')
            temp.remove('G')
            temp.remove('H')
            temp.remove('T')
            
    line = ''.join(temp)
    
    for letter in line:
        
        if(letter=='T'):
            myArray.append(3)
            temp.remove('T')
            temp.remove('H')
            temp.remove('R')
            temp.remove('E')
            temp.remove('E')
            
    line = ''.join(temp)
    for letter in line:
        
        if(letter=='F'):
            myArray.append(5)
            temp.remove('F')
            temp.remove('I')
            temp.remove('V')
            temp.remove('E')
            
            
    line = ''.join(temp)
    
    for letter in line:
        
        if(letter=='V'):
            myArray.append(7)
            temp.remove('S')
            temp.remove('E')
            temp.remove('V')
            temp.remove('E')
            temp.remove('N')
            
    line = ''.join(temp)
    
    for letter in line:
        
        if(letter=='O'):
            myArray.append(1)
            temp.remove('O')
            temp.remove('N')
            temp.remove('E')
        
            
    line = ''.join(temp)
    for letter in line:
        
        if(letter=='I'):
            myArray.append(9)
            print temp
            temp.remove('N')
            print temp
            temp.remove('I')
            print temp
            temp.remove('N')
            print temp
            temp.remove('E')
            print temp
            
            
            
            
    line = ''.join(temp)
    print line
    myArray.sort()
    print linenum
    g.write("Case #"+str(linenum)+": ")
    for i in myArray:
        g.write(str(i))
    g.write('\n')
f.close()
g.close()
        
    
#0Z,2W,4U,6X,8G
#1,3,5,7,9
#one,three,five,seven,nine
#three
#five
#seven
        