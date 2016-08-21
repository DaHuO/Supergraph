with open("inp2_py.txt","r") as fo:
	
	
	with open("out2_py.txt","w") as output:
		t=int (fo.readline().split()[0])
	
		tempt=1
		invcnt=0;
		def check_for_plus(string):
			for x in string:
				if(x!='+'):
					return False
			return True
		while(t!=tempt-1):
				string=fo.readline()
				string=list(string)
					
				string.remove('\n')
				soln=False
				while(soln==False):
					#check for plus
					
				
					if(check_for_plus(string)):
						output.write('Case #'+str(tempt)+': '+str(invcnt)+'\n')
						tempt+=1
						invcnt=0
						soln==True
						break		
					else:
						ch=string[0]
						i=1

						for x in range(1,len(string)):
							if ch!=string[x]:
								break
							i+=1
						
						for x in range(0,i):
							if(string[x]=='+'):
								string[x]='-'
							else:
									string[x]='+'

						invcnt+=1