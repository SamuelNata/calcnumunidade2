#noLinearUtils
import numpy as np

def F_1(x): #R^n->R (a raiz é um circulo de raio 1)
	#print(x)
	#print(x[0,0])
	#print(x[1,0])
	y = (x[0,0])*(x[0,0])+(x[1,0])*(x[1,0])-1
	return y

def F_2(x): #R^n->R (a raiz é a reta -x)
	y = (x[0,0])+(x[1,0])
	return y

def F_3(x): #R^n->R (a raiz é uma elipce de centro 0)
	y = x[0,0]**2+x[1,0]**2/9-1
	return y

def F_4(x): #R^n->R (a raiz é a reta y=0)
	y = x[1,0]
	return y

def F_5(x): #R^n->R (função nula)
	y = 0
	return y
