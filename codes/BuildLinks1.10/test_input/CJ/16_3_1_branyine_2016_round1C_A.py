# link: https://code.google.com/codejam/contest/dashboard?c=    #s=p0
import string
import time

testIndex=2

problemRoot="d:/prog/versenyek/googlejam"
problemDir="2016/round1C"
problemName="A"
inputFiles= ["-example.in",  "-small.in",  "-large.in"]
outputFiles=["-example.out", "-small.out", "-large.out"]

time1=time.time()
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+inputFiles[testIndex]
inputData=[map(int, line.split()) for line in open(fileName,'r') if line.strip()]
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+outputFiles[testIndex]
fileToWrite=open(fileName,'wb')
time2=time.time()
iLineNum=1
for iCase in xrange(inputData[0][0]):
  N=inputData[iLineNum][0]
  p=inputData[iLineNum+1]
  sumup=sum(p)
  nums={}
  for i in xrange(N):
    if not p[i] in nums:
      nums[p[i]]=[chr(ord('A')+i)]
    else:
      nums[p[i]].append(chr(ord('A')+i))
  maxnum=max(nums.keys())
  for i in xrange(1,maxnum):
    if i not in nums:
      nums[i]=[]
  if sumup % 2 ==1:
    part1=nums[maxnum].pop()
    if maxnum>1:
      nums[maxnum-1].append(part1)
    while maxnum>0 and not nums[maxnum]:
      del nums[maxnum]
      maxnum-=1
    solution=part1+" "
  else:
    solution=""
  both=True
  while maxnum>0:
    part1=nums[maxnum].pop()
    if maxnum>1:
      nums[maxnum-1].append(part1)
    if nums[maxnum]:
      part2=nums[maxnum].pop()
      if maxnum>1:
        nums[maxnum-1].append(part2)
      while maxnum>0 and not nums[maxnum]:
        del nums[maxnum]
        maxnum-=1
    else:
      while maxnum>0 and not nums[maxnum]:
        del nums[maxnum]
        maxnum-=1
      if maxnum>0:
        part2=nums[maxnum].pop()
        if maxnum>1:
          nums[maxnum-1].append(part2)
          while maxnum>0 and not nums[maxnum]:
            del nums[maxnum]
            maxnum-=1
    solution+=part1+part2+" "
  fileToWrite.write("Case #"+str(iCase+1)+": "+solution+"\n")
  iLineNum+=2
fileToWrite.close()
print 'Total time:   ', time.time() - time1
print 'Solving time: ', time.time() - time2
