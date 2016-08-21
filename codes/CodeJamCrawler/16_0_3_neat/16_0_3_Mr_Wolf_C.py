from random import randrange
from math import sqrt

primos = []

#first million primes downloaded from: 
#https://primes.utm.edu/lists/small/millions/
def carregarPrimos():
	with open("primes1.txt") as f:
		for linha in f:
			for el in linha.split():
				primos.append(int(el))

def gerarNumero(N):
	numero = ["1"];
	for i in range(N-2):
		numero.append(str(randrange(2)));
	numero.append("1");
	return "".join(numero);

def naoEhPrimo(numero):
	for el in (i for i in primos if numero%i==0):
		return el

def provaCoinJam(numero):
	provas = []
	for base in range(2, 11):
		atual = int(numero, base)
		p = naoEhPrimo(atual)
		if (p and p != atual):
			provas.append(p)
		else:
			return []
	return provas

def resolver(N, J):
	carregarPrimos()
	print("Case #1:")
	S = set()
	jcs = 0
	numero = gerarNumero(N)
	while(jcs < J):
		while (numero in S):
			numero = gerarNumero(N)
		S.add(numero)

		provas = provaCoinJam(numero)
		if (provas):
			jcs += 1
			print(numero, end=" ")
			for el in provas:
				print(el, end=" ")
			print()

T, (N, J) = input().split(), input().split()
N, J = int(N), int(J)
resolver(N, J)