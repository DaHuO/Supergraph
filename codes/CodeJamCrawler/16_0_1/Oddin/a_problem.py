#!/usr/bin/python
import sys

cases = int(sys.stdin.readline().rstrip("\n"),10)


for c in range(0,cases):
	answer="INSOMNIA"
	BITRIX=int(sys.stdin.readline().rstrip("\n"),10)
	MAIN_BITRIX=BITRIX
	num_dic={}
	i=1
	if BITRIX!=0:

		while len(num_dic.keys())!=10:	
		
			for alpha in str(BITRIX):
				num_dic[alpha]=alpha

			if len(num_dic.keys())==10:
				break
			else:
				i=i+1	
				BITRIX=i*MAIN_BITRIX


		answer=str(BITRIX)		
		
		

	print("Case #"+str(c+1)+": "+answer)
