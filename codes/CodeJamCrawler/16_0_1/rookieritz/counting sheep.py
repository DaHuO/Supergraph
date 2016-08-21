file = open('A-large.in', 'r+')
file_output= open('output.txt','w+')

sheep=""

test_cases=int(file.readline())
for i in range(1,test_cases+1):
    file_output.write("Case #{}: ".format(i))
    sheep=int(file.readline())
    flag_bits=[0,0,0,0,0,0,0,0,0,0]
    flag=0

    if int(sheep)==0:
        file_output.write("INSOMNIA")
    else:
        count = 1
        while(flag==0):
            print(sheep)
            temp_sheep = sheep * count
            count += 1
            temps_sheep=str(temp_sheep)
            for ch in temps_sheep:
                flag_bits[int(ch)]=1
            print(temps_sheep)
            print(flag_bits)
            flag=1
            for bit in flag_bits:
                if bit==0:
                    flag=0
        file_output.write(str(temp_sheep))
    if(i!=test_cases):
        file_output.write("\n")

file.close()
file_output.close()
