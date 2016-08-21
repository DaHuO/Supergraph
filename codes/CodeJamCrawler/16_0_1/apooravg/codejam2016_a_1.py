import re
import time
#start_timer = time.time()
file=open("A.in","r")
filer=file.read()
fr=re.findall("\d+",filer)
file.close()
fw=open("A-out.txt","w")
t=int(fr[0])
counter=1
output=""
for i in range(1,(t+1)):
	# Each new case begins
	#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	flag=0
	num=set(['0','1','2','3','4','5','6','7','8','9'])
	n=int(fr[counter])
	temp=n
	#print("n"+str(n))
	counter=counter+1
	#change time_span 
	time_span=2.4
	stop = time.time()+time_span
	while time.time() < stop:
		digits=set(re.findall("\d",(str(temp))))
		#print("digits" + str(digits))
		#delete the digits
		num=num-digits
		#print("num ="+ str(num))
		if not num:
			output=output+"Case #"+str(i)+": "+str(temp)+"\n"
			flag=1
			break
		temp=temp+n
		#print("ïncr  "+str(temp)) 
	if flag==0:
		output=output+"Case #"+str(i)+": "+"INSOMNIA"+"\n"
fw.write(output)
fw.close()
stop_timer = time.time()
#print(stop_timer-start_timer)
		

  		
