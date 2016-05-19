from math import *
#import numpy as np

#seno de x = sin(x)
#cosseno de x = cos(x)
#logaritmo de x base b (base opcional, se n for especficada sera e) = log(x, b)
#e^x = math.exp(x)
#pi = math.pi
#e = math.e

#DECLARACAO DA FUNCAO
def f(x):
	#y = exp(-x) - x
	y = x**2 -2.5*x - 3.5
	return y

#CALCULO DA DERIVADA (NAO PRECISA SER ALTERADO QUANDO ALTERAR O f(x))
def f_(x):
	h = 0.00001
	y = (f(x+h)-f(x))/h
	return y


def g(x):
	y = exp(-x)
	#y = (x**2+3)/10
	return y


def g_(x):
	h = 0.00001
	y = (g(x+h)-g(x))/h
	return y
'''
def f1(x):
	#print(x)
	#print(x[0,0])
	#print(x[1,0])
	y = (x[0,0])*(x[0,0])+(x[1,0])*(x[1,0])-1
	return y

def f2(x):
	y = (x[0,0])+(x[1,0])
	return y


def F(x):
	m = np.asmatrix([f1(x), f2(x)]).T;
	return m
'''