d=[3, 2, 3, 2, 7, 2, 3, 2, 3];

def check(x,b):
  m=0
  for i in range(32):
  	if x>>i&1:
  		m+=pow(b,i)
  return m%d[b-2]

print("Case #1:");
start = pow(2,31)+1
k=500
while k>0:
	f=0
	for i in range(2,11):
		f=f|check(start, i)
	if f==0:
		k-=1
		print("{0:b}".format(start)),
		print("3 2 3 2 7 2 3 2 3")
	start+=2