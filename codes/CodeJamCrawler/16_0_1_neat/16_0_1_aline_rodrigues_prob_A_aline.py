import sys

read_file = open(sys.argv[1],"r")
items = read_file.readlines()
write_file = open(sys.argv[2],"w")
for j in xrange(1,int(items[0])+1):
    N = int(items[j])
    calc = last_calc = ''
    i = 1
    vector = []
    while len(vector)<10:
        last_calc = calc
        calc = list(str(i*N))
        for item in calc:
            if (item in vector)==False:
                vector.append(item)
        if calc==last_calc:
            write_file.write('Case #'+str(j)+': INSOMNIA\n')
            break
        i+=1
    if calc!=last_calc:
        write_file.write('Case #'+str(j)+': '+''.join(calc)+'\n')
        
write_file.close()