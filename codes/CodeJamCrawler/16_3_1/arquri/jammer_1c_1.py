import sys, os
import requests
import urllib
import types
import re
import math
from operator import itemgetter

handle = open("A-small-attempt0 (1).in","r")
allconts = handle.read().split("\n")
handle.close()

T = int(allconts[0])
results = []

for i in range(0,T):
	N = int(allconts[1+(i*2)])
	parts = allconts[2+(i*2)].split(" ")
	for k in range(0,N):
		parts[k] = float(parts[k])
	# in each step of removal, we have to remove as many as possible, without allowing a majority
	removals = []
	
	for q in range(0,10):
		# check if we are at only two guys left
		if sum(parts)==2:
			netstr = ""
			for r in range(0,N):
				if parts[r]==1:
					netstr = netstr + chr(65+r)
			removals.append(netstr)
			break
	
		# begin the removal process
		deleteMults = False
		for m in range(0,N):
			isvalid = True
			# attempt to remove
			newarr = parts[:]
			newarr[m] = newarr[m]-1
			# check if this is permitted
			#newarr = newarr/sum(newarr)
			totals = sum(newarr)
			temparr = newarr
			for r in range(0,N):
				temparr[r] = temparr[r]/totals
			newarr = temparr
			for r in range(0,N):
				if newarr[r]>0.5:
					isvalid = False
					break
			if isvalid==True:
				# this one is fine
				removals.append(chr(65+m))
				parts[m] = parts[m]-1
				break
			if m==(N-1):
				# couldn't find any valid pairing by single deletions
				# we have to delete multiples
				deleteMults = True
		
		if deleteMults==True:
			for m in range(0,N):
				for q in range(m+1,N):
					isvalid = True
					# attempt to remove
					newarr = parts[:]
					newarr[m] = newarr[m]-1
					newarr[q] = newarr[q]-1
					# check if this is permitted
					#newarr = newarr/sum(newarr)
					totals = sum(newarr)
					temparr = newarr
					for r in range(0,N):
						temparr[r] = temparr[r]/totals
					newarr = temparr
					for r in range(0,N):
						if newarr[r]>0.5:
							isvalid = False
							break
					if isvalid==True:
						# this one is fine
						removals.append(chr(65+m)+chr(65+q))
						parts[m] = parts[m]-1
						parts[q] = parts[q]-1
						break
				if isvalid==True:
					break
	
	
	results.append(removals)
	print removals
	
#print removals
handle = open("jammer_1c_1.txt","w")
for i in range(0,len(results)):
	handle.write("Case #"+str(i+1)+": "+" ".join(results[i])+"\n")
handle.close()
	
	