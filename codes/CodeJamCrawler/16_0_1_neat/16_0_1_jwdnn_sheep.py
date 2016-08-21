#Revenge of the sheep

inputFile = open("A-large.in",'r')
out = open('outSheep.out','w')
tests = int(inputFile.readline().strip())

for i in range(tests):
    digits = []
    multiply = 1
    num = int(inputFile.readline().strip())
    while len(digits) < 10:
        if num == 0:
                out.write("Case #%d: "%(i+1)+"INSOMNIA\n") 
                break
        for digit in str(num*multiply):
            if digit not in digits:
                digits.append(digit)        
        multiply+= 1
    if num != 0:
        out.write("Case #%d: "%(i+1) + str(num*(multiply-1))+"\n")
    
inputFile.close()
out.close()
    
    