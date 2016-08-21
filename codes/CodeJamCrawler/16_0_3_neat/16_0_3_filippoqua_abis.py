n = 32
b = []
j = 500
np = 0
nd = 0

out_file = open("output.txt","w")

def trasforma(base):
	global n
	global b
	ris = 0
	for i in range(n):
		if b[i]==1:
			ris=ris+base**i
	return ris

def trovaDivisore(numero):
	i=2
	while i*i<=numero:
		if numero%i==0:
			return i
		i=i+1
	return -1

def prova(pos):
	global b
	global n
	global np
	global nd
	global j
	if j<=0:
		return
	if pos==n-1:
		if pos%2==0:
			np=np+1
		else:
			nd=nd+1
		b[pos]=1
		if not (np%3!=0 or nd%3!=0 or (np+nd)%2!=0):
			divisore6 = trovaDivisore(trasforma(6))
			if divisore6!=-1:
				i = n-1
				while i>=0:
					out_file.write(str(b[i]))
					i=i-1
				for i in range(2,11):
					if i%3!=0:
						out_file.write(" 3")
					elif i!=6:
						out_file.write(" 2")
					else:
						out_file.write(" "+str(divisore6))
				out_file.write("\n")
				j=j-1
		if pos%2==0:
			np=np-1
		else:
			nd=nd-1
	else:
		if pos!=0:
			b[pos] = 0
			prova(pos+1)
		if pos%2==0:
			np=np+1
		else:
			nd=nd+1
		b[pos] = 1
		prova(pos+1)
		if pos%2==0:
			np=np-1
		else:
			nd=nd-1
			
out_file.write("Case #1:\n");

for i in range(n):
	b=b+[0]
prova(0)
