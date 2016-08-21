T=int(raw_input())
for i in range(1,T+1):
	asd=raw_input()
	nuevo=asd[0]
	for j in range(1,len(asd)):
		if nuevo[0]=="1" or nuevo[0]=="2" or nuevo[0]=="3" or nuevo[0]=="4" or nuevo[0]=="5" or nuevo[0]=="6" or nuevo[0]=="7" or nuevo[0]=="8" or nuevo[0]=="9" or nuevo[0]=="0":
			nuevo=nuevo+asd[j]
		elif asd[j]=="1" or asd[j]=="2" or asd[j]=="3" or asd[j]=="4" or asd[j]=="5" or asd[j]=="6" or asd[j]=="7" or asd[j]=="8" or asd[j]=="9" or asd[j]=="0":
			nuevo=asd[j]+nuevo
		elif asd[j]<nuevo[0]:
			nuevo=nuevo+asd[j]
		else:
			nuevo=asd[j]+nuevo
	print "Case #"+str(i)+": "+nuevo
