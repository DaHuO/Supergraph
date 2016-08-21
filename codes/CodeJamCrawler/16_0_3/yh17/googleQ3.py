import math
import sys
array1 =[]
created=''
list1=[]

def createInput(size, loop):
	global created
	input2 = ''
	a= bin(loop)[2:]
	#print('--------------------------------------------------')
	created = '1'+str(a).zfill(size-2)+'1'

	return '1'+str(a).zfill(size-2)+'1'

def createBase(createBase_input):
	
	array1.append(int(createBase_input,2))
	array1.append(int(createBase_input,3))
	array1.append(int(createBase_input,4))
	array1.append(int(createBase_input,5))
	array1.append(int(createBase_input,6))
	array1.append(int(createBase_input,7))
	array1.append(int(createBase_input,8))
	array1.append(int(createBase_input,9))
	array1.append(int(createBase_input,10))
	#print('array',array1)

def primeCheck(primeCheck_input):
	if primeCheck_input >= 2:
		checkUpTo = int(math.sqrt(primeCheck_input))
		for y in range(2,checkUpTo):
			#print('looping:',primeCheck_input,primeCheck_input%2,y)
			if primeCheck_input % y ==0:
				return y
			
	else:
		return False 
	return True	
whatISay=[]
found_count = 0
up = 0
def main(main_size):
	global found_count
	global array1 
	global up
	global whatISay
	primeResult=[]
	up+=1
	array1 = []
	
	if found_count == findHowMany:
		#print('it worked wwtwt')
		
		final_answer= 'Case #'+list1[0].strip()+':'
		sys.stdout.write(final_answer+'\n')
		
		#print(whatISay)
		
		for x in range(0,len(whatISay)):
			sys.stdout.write(whatISay[x]+'\n')
		
		sys.exit(0)
	else:
		#print('creating')
		input =createInput(main_size,up)
		createBase(input)
		for x in range (0,len(array1)):
			#print(array1,'looping')
			if primeCheck(array1[x])== True:
				#print('ran')
				main(main_size)
			else:	
				primeResult.append(primeCheck(array1[x]))
			
		if not True in primeResult:
			whatISay.append(created+" "+" ".join(str(x) for x in primeResult))
			#final_answer = 'Case #'+str(caseNumber)+': '+str(answer)+'\n'
			#sys.stdout.write(final_answer)
			found_count += 1
			#print('Correct',primeResult)
			#print('--------------------------------------------------')
			main(main_size)
		else:
			main(main_size)

list1=[]
for line in sys.stdin:
	list1.append(line)

first = list1[1].split()

findHowMany	=int(first[1])
main(int(first[0]))


