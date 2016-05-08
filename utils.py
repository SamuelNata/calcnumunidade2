import math
#seno de x = sin(x)
#cosseno de x = cos(x)
#logaritmo de x base b (base opcional, se n for especficada será e) = log(x, b)
#e^x = math.exp(x)
#pi = math.pi
#e = math.e

#DECLARAÇÃO DA FUNÇÃO
def f(x):
	y = x**2+3*x-10
	return y

#CALCULO DA DERIVADA (NÃO PRECISA SER ALTERADO QUANDO ALTERAR O f(x))
def f_(x):
	h = 0.00001
	y = (f(x+h)-f(x))/h
	return y
	
def fNoPonto(poli, ponto):
	
	soma = 0
	grau = len(poli)
	#print('Calculando f({})...'.format(ponto))
	for i in range(grau):
		soma = soma + poli[i] * (ponto**(grau-i-1))
	return soma

def fLinNoPonto(poli, ponto):
	pass
