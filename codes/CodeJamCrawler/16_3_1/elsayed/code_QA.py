with open('input.txt') as input_file:
    lines = input_file.readlines()
    
txt = open("output.txt", "ab")

case = []
N_lines = 1
N_case = int(lines[0])

for i in range(1,(N_case*2), 2):
    case.append(lines[i+1].split())

for i in range(0,N_case, 1):
    arr=[]
    flist = []
    fflist = []
    out = ""
    for ch in case[i]:
        arr.append(int(ch))

    while sum(arr) > 0:
        #print arr
        (m,k) = max((v,k) for k,v in enumerate(arr))
        arr[k] = arr[k]-1
        flist.append(chr(k+65))
    
    if(len(flist))%2 != 0:
        out = flist[0]+" "
        for m in range(1, len(flist), 2):
            out = out+flist[m]+flist[m+1]+" "
            #fflist.append(flist[m]+flist[m+1])
            m = m+1
    else:
        for m in range(0, len(flist), 2):
            #print m, m+1
            #m = m+1
            out = out+flist[m]+flist[m+1]+" "
            #fflist.append(flist[m]+flist[m+1])
            m = m+1
        
    #print flist
    output =  "Case #"+str(i+1)+": "+out+"\n"
    print output
    txt.write(output)

txt.write(output)   
#print (m,i) #(5, 2)
    #for i in range(0, len(arr)):
        

    #output =  "Case #"+str(i+1)+": "+''.join(out)+"\n"
    #print output
#
       
       
#txt.close
