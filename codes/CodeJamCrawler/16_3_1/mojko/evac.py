import numpy as np
import copy 
def check_2(nums,j):
	nums2 = copy.copy(nums)
	nums2[j] = nums2[j] - 2
	T = sum(nums2)
	if (T>0):
		for element in nums2:
			if (element/float(T))>0.5:
				#print "Check 2: Majority detected, ", element, (element/float(T))  
				return 0
		return 1
	else:
		return 1



def check_1(nums,j,k):
	nums2 = copy.copy(nums)
	nums2[j] = nums2[j] - 1
	nums2[k] = nums2[k] - 1
	T = sum(nums2)
	if (T>0):
		for element in nums2:
			if (element/float(T))>0.5:
				#print "Check 1: Majority detected, ", element ,(element/float(T))
				return 0
		return 1
	else:
		return 1

T = raw_input('')
for i in np.arange(0,int(T),1):
	N = raw_input('')
	nums = np.array(map(int, raw_input('').split(" ")))
	

	seq = []

	while (np.sum(nums)>0):
		candidates = nums.argsort()[-2:]
		#print "Nums", nums
		#print "Best 2",candidates
		## Remove 2 from largest
		if (nums[candidates[0]]>=2) and (check_2(nums,candidates[0])==1):
			#print "Removing 2"
			nums[candidates[0]]=nums[candidates[0]]-2
			seq.append([str(chr(candidates[0]+65)),str(chr(candidates[0]+65))])
		## Remove 1 from largest and 1 from second largest
		elif (nums[candidates[0]]>=1) and (nums[candidates[1]]>=1) and (check_1(nums,candidates[0],candidates[1])==1):
			#print "Removing 1"
			nums[candidates[0]]=nums[candidates[0]]-1
			nums[candidates[1]]=nums[candidates[1]]-1
			seq.append([str(chr(candidates[0]+65)),str(chr(candidates[1]+65))])
		else:
			#print "Removing 0"
			nums[candidates[0]]=nums[candidates[0]]-1
			seq.append(chr(candidates[0]+65))
		
	#print seq

	print "Case #" + str(i+1)+":",
	for element in seq:
		print "".join(element),
	#print "================================="
	print 