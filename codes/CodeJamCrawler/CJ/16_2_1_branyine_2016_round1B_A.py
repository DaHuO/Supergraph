# link: https://code.google.com/codejam/contest/dashboard?c=    #s=p0
import string
import time

testIndex=2

problemRoot="d:/prog/versenyek/googlejam"
problemDir="2016/round1B"
problemName="A"
inputFiles= ["-example.in",  "-small.in",  "-large.in"]
outputFiles=["-example.out", "-small.out", "-large.out"]

time1=time.time()
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+inputFiles[testIndex]
inputData=[map(str, line.split()) for line in open(fileName,'r') if line.strip()]
fileName=string.strip(problemRoot)+"/"+problemDir+"/"+problemName+outputFiles[testIndex]
fileToWrite=open(fileName,'wb')
time2=time.time()
iLineNum=1
for iCase in xrange(int(inputData[0][0])):
  numStr=inputData[iLineNum][0]
  # Z num of zeros
  # W num of twos
  # U num of fours
  # X num of sixes
  # G num of eights
  # F num minus fours is num fives
  # V num minus fives is num sevens
  # R num minus zeros minus fours is num threes
  # I num minus fives minus sixes minus eights is num nines
  # N num minus sevens minus nines*2 is num ones
  numChs={}
  for ch in 'ZWUXGFVRIN':
    numChs[ch]=0
  for ch in numStr:
    if ch in 'ZWUXGFVRIN':
      numChs[ch]+=1
  nums=[0]*10
  nums[0]=numChs['Z']
  nums[2]=numChs['W']
  nums[4]=numChs['U']
  nums[6]=numChs['X']
  nums[8]=numChs['G']
  nums[5]=numChs['F']-nums[4]
  nums[7]=numChs['V']-nums[5]
  nums[3]=numChs['R']-nums[0]-nums[4]
  nums[9]=numChs['I']-nums[5]-nums[6]-nums[8]
  nums[1]=numChs['N']-nums[7]-2*nums[9]
  toCall=''
  for i in xrange(10):
    toCall+=str(i)*nums[i]
  print toCall
  fileToWrite.write("Case #"+str(iCase+1)+": "+toCall+"\n")
  iLineNum+=1
fileToWrite.close()
print 'Total time:   ', time.time() - time1
print 'Solving time: ', time.time() - time2
