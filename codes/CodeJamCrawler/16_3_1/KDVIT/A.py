def checkEqual2(iterator):
			return len(set(iterator)) <= 1
def check_all_one(a):
       		for x in a:
       			if x!=1:
       				return False
       		return True
def check_all_zero(a):
			for x in a:
				if x!=0:
					return False
			return True
		

with open("Ain.txt","r") as fo:
	
	
	with open("Aout.txt","w") as output:
		


		test=int (fo.readline().split()[0])
		temp1=1;
		
		while(temp1!=test+1):
				N=int (fo.readline().split()[0])
				sen=[]
				ans=[]
				dic_a={}
				dic_c={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
				ppl=fo.readline().split()
				for x in ppl:
					sen.append(int(x))
				for x in xrange(0,len(sen)):
					dic_a[x]=dic_c[x]*sen[x]

				if N==2:
					while check_all_zero(sen)==False:
						
						if checkEqual2(sen):
							
							while(check_all_zero(sen)==False):
								ans.append(dic_c[0]+dic_c[1])
								sen[0]-=1
								sen[1]-=1
								
						else:
							mma=max(sen)
							mi=[i for i, j in enumerate(sen) if j == mma]
							mi=mi[0]
							sen[mi]-=1
							ans.append(dic_c[mi])

				
				else:

					while(check_all_zero(sen)==False):
						if(check_all_one(sen)==True):
							if len(sen)%2==0:
								for y in xrange(0,len(sen),2):
									ans.append(dic_c[y]+dic_c[y+1])
									sen[y]-=1
									sen[y+1]-=1
							else:
								sen[0]-=1
								ans.append(dic_c[0])
								for y in xrange(1,len(sen),2):
									ans.append(dic_c[y]+dic_c[y+1])
									sen[y]-=1
									sen[y+1]-=1

						else:
							mma=max(sen)
							mi=[i for i, j in enumerate(sen) if j == mma]
							mi=mi[0]
							sen[mi]-=1

							ans.append(dic_c[mi])
						
				ansf=""
				for x in ans:
					ansf=ansf+x+' '
				output.write('Case #'+str(temp1)+': '+ansf+'\n')
				temp1+=1