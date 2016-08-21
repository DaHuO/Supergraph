import sys, os
import requests
import urllib
import types
import re
import math
from operator import itemgetter

handle = open("A-large.in","r")
allconts = handle.read().split("\n")
handle.close()

T = int(allconts[0])
results = []
for i in range(0,T):
	N = int(allconts[i+1])
	if N==0:
		results.append("INSOMNIA")
		continue
	remdigs = range(0,10)
	useddigs = []
	for m in range(1,50000):
		digs = str(N*m)
		for k in range(0,len(digs)):
			if not digs[k] in useddigs:
				useddigs.append(digs[k])
			if len(useddigs)==10:
				break
		if len(useddigs)==10:
			break
	results.append(N*m)
	
handle = open("jam_results2.txt","w")
for i in range(0,T):
	handle.write("Case #"+str(i+1)+": "+str(results[i])+"\n")
handle.close()

