#input_file=open("in.txt")
#output_file=open("out.txt",'w')
#test = int(input_file.readline())



##the program takes a number as a string. Splits thsi string into a list of characters. Then comapre the character whith the num_list. 
test = int(input())
j = 1
flag = 0
while (j<=test):
    num_list = ['0','1','2','3','4','5','6','7','8','9']
    #n = input_file.readline()
    n = input() #takes input as string
    num = n
    i = 1
   
        
    while(len(num_list)>0):
        if(int(num)==0):
            #output_file.write
            print("Case #"+str(j)+": INSOMNIA")
            break
        else:
            flag = 1
        num = str(int(n)*i)
        n_list = list(num) #splits the string into list of characters. e.g '123'---> ['1','2','3']
        match = set(num_list).intersection(n_list) # find the match between two lists by intersection of sets
        num_list = list(set(num_list)-set(match)) #remove matched numbers from num_list
        i = i+1
    if(flag == 1):
        #output_file.write
        print("Case #"+str(j)+": "+num+"")
    
    j = j+1
#input_file.close()
#output_file.close()
