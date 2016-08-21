def reverse(x):
    x = x[::-1]
    y = ['+' if i == '-' else '-' for i in x]
    return ''.join(y)
            

def answer(x):
    result = 0
    pointer = len(x) - 1
    while pointer >= 0:
        #print(result, x)
        if x[pointer] == '+':
            pointer -= 1 
        else:
            if x[0] == '-':
                x = reverse(x[:pointer + 1]) + x[pointer + 1:]
                result += 1
            else:
                x = reverse(x[:pointer + 1]) + x[pointer + 1:]
                while pointer >= 0 and x[pointer] == '-':
                    pointer -= 1
                pointer -= 1
                result += 2 
                
                
    return result
            

fin = open('B-large.in', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())
for i in range(t):
    print('Case #' + str(i + 1) + ': ' + str(answer(fin.readline().split()[0])))
    
fout.close()
    