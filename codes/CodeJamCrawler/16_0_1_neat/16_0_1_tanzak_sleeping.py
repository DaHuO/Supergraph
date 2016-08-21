# -*-coding:UTF-8 -*

def recursive_multplication(N):
        l=[]
        j=1
        while (len(l) != 10):
                for i in range(len(str(N*j))):
                        if (str(N*j)[i] not in l):
                                l.append(str(N*j)[i])
                j=j+1
        return N*(j-1)



def sleeping():
        input_file=open('A-large.in','r')
        output_file=open('A-large.out','w')
        T = input_file.readline()
        for t in range(int(T)):
                N=int(input_file.readline())
                if N == 0:result="INSOMNIA"
                else: result= recursive_multplication(N)
                output_file.write('Case #{}: {} \n'.format(t+1,result))
        input_file.close()
        output_file.close()

    	#print N
    	#print 'Case #{}:'.format(t+1) 
      
      
                

   
        
if __name__ == "__main__":
    sleeping()
    #os.system("pause")

