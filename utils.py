from math import *
import numpy as np

#seno de x = sin(x)
#cosseno de x = cos(x)
#logaritmo de x base b (base opcional, se n for especficada será e) = log(x, b)
#e^x = math.exp(x)
#pi = math.pi
#e = math.e

#DECLARAÇÃO DA FUNÇÃO
def f(x):
	y = exp(-x) - x
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


def g(x):
	y = exp(-x)
	return y


def g_(x):
	h = 0.00001
	y = (g(x+h)-g(x))/h
	return y

def f1(x):
	#print(x)
	#print(x[0,0])
	#print(x[1,0])
	y = (x[0,0])*(x[0,0])+(x[0,1])*(x[0,1])-1
	return y

def f2(x):
	y = (x[0,0])+(x[0,1])
	return y


def F(x):
	m = np.asmatrix([f1(x), f2(x)]).T;
	return m
