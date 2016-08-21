input_data = open('/Users/MaNTi/Desktop/A-large.in')
input_data= input_data.read().splitlines()

T = int(input_data[0])
f = open('outputlarge.in','w')

for each in range(1,T+1):
    map1 = [0,0,0,0,0,0,0,0,0,0]
    counter = 1
    num = int(input_data[each])
    if num ==0:
        f.write("Case #"+str(each) +': '+  "INSOMNIA"+'\n')
        continue
    while sum(map1) < 10:
        num_temp =num*counter
        temp = [int(i) for i in str(num_temp)]
        for n in temp:
            map1[n] = 1
        counter +=1
    if sum(map1) >= 10:
        f.write("Case #"+str(each) +': '+ str(num_temp)+'\n')
        
