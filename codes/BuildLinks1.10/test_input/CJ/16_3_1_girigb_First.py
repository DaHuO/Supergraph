import heapq

T = int(raw_input())
counter = 1
while T>0:
	data = []
	result = [] 
	N = int(raw_input())
	TOTAL = 0
	nums = map(int,raw_input().split())
	for i,num in enumerate(nums):
		TOTAL += num
		val = (-1*int(num),chr(65+i))
		heapq.heappush(data,val)
	# print data
	# print data,TOTAL
	while TOTAL > 0:
		send = []
		string =""
		
		if TOTAL != 2 :
			# print "in first ", TOTAL ,"is total"
			p,ch = heapq.heappop(data)
			p = int(p)
			send.append(ch)
			p+=1
			TOTAL-=1
			heapq.heappush(data,(p,ch))
		else:
			# only two left 
			p1,ch1 = heapq.heappop(data)
			p2,ch2 = heapq.heappop(data)
			string = ch1+ch2
			send.append(string)
			TOTAL-=2
		# print "after first ", data ,"is data"


		if TOTAL > 2 :
			# print "in second ", TOTAL ,"is total"
			p,ch = heapq.heappop(data)
			p = int(p)
			send.append(ch)
			p+=1
			TOTAL-=1
			heapq.heappush(data,(p,ch))

		# print "after  second ", data ,"is data"


		# string  = send.join('')
		
		string = ''.join(send)

		result.append(string)
	# print "result is ",result
	print "Case #"+str(counter)+":",
	for i in result:
		print i+" ",
	print ""





	


	counter+=1

	T-=1
