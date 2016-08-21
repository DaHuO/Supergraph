g = open('D:\Users\john\My Documents\Google Code Jam\Google Code Jam 2016\sheep_small_out.txt','w+')

with open('D:\Users\john\My Documents\Google Code Jam\Google Code Jam 2016\A-small-attempt0.in', 'r+') as f:
    num_cases = int(f.readline())
    
    for i in range(num_cases):
        number = int(f.readline())
        
        j = 1
        digits_seen = []
        done = False
        
        if number != 0:
            while(not done):
                new_num = j * number
                new_num_str = str(new_num)

                digits = list(new_num_str)
                digits_seen = np.union1d(digits_seen, digits)
                digits_seen = np.unique(digits_seen)

                if(len(digits_seen) == 10):
                    done = True
                else:
                    j += 1
        else:
            new_num_str = 'INSOMNIA'
                
        g.write('Case #' + str(i+1) + ': ' + new_num_str + '\n')
        
g.close()