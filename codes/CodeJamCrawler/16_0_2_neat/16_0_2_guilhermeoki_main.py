'''
Created on 09/04/2016

@author: gandalf
'''


def pancakes(stringInput):
    tamanho = 0
    ultimo_menos = 0
    
    for i in range(0,len(stringInput)):
        if  i == 0 or stringInput[i] != stringInput[i -1]:
            tamanho +=1
            
            if stringInput[i] == '-':
                ultimo_menos = tamanho
    
    return ultimo_menos

def main():
    T = input()
    T += 1
    for i in range(1,T):
        stringInput = raw_input()
        
        result = pancakes(stringInput)
        
        print "Case #%d: %d" % (i,result)

if __name__ == '__main__':
    main()