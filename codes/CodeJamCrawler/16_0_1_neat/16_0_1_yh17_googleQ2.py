import sys


count =0
checkArray =''
string_word =''

def recursive(recursive_input):
	global count
	global string_word
	count +=1
	
	if recursive_input == '0':
		return 'INSOMNIA' 
	else:
		int_input = int(recursive_input)*count
		string_intput =str(int_input)
		string_word =string_word+ string_intput
		
		
		words = list(string_word)
		#print(words)
		
		if check(words)==1:
			return int_input
		else:
			return recursive(recursive_input)
	
	

def check(checkItem):
	if '0' in checkItem and '1' in checkItem and '2' in checkItem and '3' in checkItem and '4' in checkItem and '5' in checkItem and '6' in checkItem and '7' in checkItem and '8' in checkItem and '9' in checkItem:
		#print ('SUCCESS')
		return 1
	else:
		#print('FAIL')
		return 0


list1=[]
for line in sys.stdin:
	list1.append(int(line))


howmanyrun = list1[0]
#print(list1)
caseNumber = 1

for x in range (1,howmanyrun+1):
	
	input = str(list1[x])
	count =0
	checkArray =''
	string_word =''
	answer = recursive(input)
	final_answer = 'Case #'+str(caseNumber)+': '+str(answer)+'\n'
	sys.stdout.write(final_answer)
	caseNumber += 1



	
