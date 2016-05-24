from __future__ import division
from math import *
#import numpy as np

#seno de x = sin(x)
#cosseno de x = cos(x)
#logaritmo de x base b (base opcional, se n for especficada sera e) = log(x, b)
#e^x = math.exp(x)
#pi = math.pi
#e = math.e

#=======================================================================
#DECLARACAO DA FUNCAO
def f1(x, info = False, poli = False):
	if(poli):
		return [0]
	if(info):
		print('f(x) = e^(-x) - x')
		print('Raiz exata: 0,56714329')
		return 0
	y = exp(-x) - x
	return y

def f2(x, info = False, poli = False):
	if(poli):
		return [1,-102,200]
	if(info):
		print('f(x) = x^2 - 102x + 200')
		print('Raiz exata: 100 e 2')
		return 0
	y = x**2 -102*x + 200
	return y

def f3(x, info = False, poli = False):
	if(poli):
		return [1,0,-25]
	if(info):
		print('f(x) = x^2 - 25')
		print('Raiz exata: 5 e -5')
		return 0
	y = x**2 - 25
	return y

#=======================================================================
#CALCULO DA DERIVADA (NAO PRECISA SER ALTERADO QUANDO ALTERAR O f(x))
def f_(f, x):
	h = 0.00001
	y = (f(x+h)-f(x))/h
	return y

#=======================================================================
#DECLARANDO AS Gs
def g1c(x, info = False):
	if(info):
		print('g(x) = e^(-x)')
		return 0
	y = exp(-x)
	return y

def g1d(x, info = False):
	if(info):
		print('g(x) = ?')
		return 0
	y = 0
	return y

#............................
def g2c(x, info = False):
	if(info):
		print('g(x) = 102 - 200/x')
	if(x==0): x = 0.0000000000000000001 # gambiarra pra eviar divisão por 0
	y = 102 - 200/x
	return y

def g2d(x, info = False):
	if(info):
		print('g(x) = x^2 - 101x + 200')
	y = x**2 -102*x + 200
	return y

#............................
def g3c(x, info = False):
	if(info):
		print('g(x) = ?')
		return 0
	if(x==0): x = 0.0000000000000000001 # gambiarra pra eviar divisão por 0
	y = 0
	return y

def g3d(x, info = False):
	if(info):
		print('g(x) = x^2 + x - 25') # 25/x tambem diverge
		return 0
	if(x==0): x = 0.0000000000000000001 # gambiarra pra eviar divisão por 0
	y = x**2 + x - 25
	return y

#............................

def g_(g, x):
	h = 0.00001
	y = (g(x+h)-g(x))/h
	return y
