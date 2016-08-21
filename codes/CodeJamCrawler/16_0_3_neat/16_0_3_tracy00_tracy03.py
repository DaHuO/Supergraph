def generation(jodi,leng):

	for i in range(1,leng-1):
		
		if(jodi[i]=='1'):

			jodi[i]='0'
		
		else:

			jodi[i]='1'

			break
	
def result(jodi,nos,nut):

	fin = [0 for i in range(11)]

	for i in range(2,11):

		nos[i]=i

		fin[i]=1
		
	for i in range(1,nut):

		if(jodi[i]=='1'):

			for i in range(2,11):

				fin[i]+=nos[i]

				nos[i]=nos[i]*i

		else:

			for i in range(2,11):

				nos[i]=nos[i]*i

	sf="".join(jodi)

	sf=sf[::-1]

	
	print(sf+sf),

	for i in range(2,11):

		print fin[i],
	print ""			
				


#google code jam
test = raw_input()

test=int(test)

				
cut=0

for i in range(test):

	cut=1+cut

	print("Case #"+str(cut)+":")

	nut,j = map(int,raw_input().split())

	nut = nut//2

	s2 = ['0' for i in range(nut)]

	s2[0]='1'

	s2[nut-1]='1'
	
	count = 0

	nos = [0 for i in range(11)]

	while (count<j):

		count=count+1

		generation(s2,nut)	
		
		result(s2,nos,nut)
