import math
import time
from utils import *
import numpy as np

def getI(x):
	n = len(x)
	ident = np.asmatrix(np.zeros(shape=(n,n)))
	for i in range(n):
		ident[i,i] = 1
	return ident

def getNorma(x):
	t = 0
	for i in range(x.shape[0]):
		t = t + x[i,0]
	return sqrt(t)

	#todas as matrizes são iniciadas com string
def broyden(x, erro): # x é o chute inicial no formato de string, e erro é o erro maximo esperado
	xap = np.asmatrix(x).T;
	bap = getI(x)
	bapM1 = getI(x)
	iteracao = 1
	erroAtual = 1000000
	#print 'erro: ', getNorma(xap-baux)
	while erroAtual>=erro :
		xnovo = xap - np.dot(bapM1,F(xap))
		deltaF = F(xnovo)-F(xap)
		deltaX = xnovo - xap
		u = ln.linalg.lstsq((deltaF-np.dot(bap,deltaX)),ln.dot(deltaX.T,deltaX))
		baux = bap
		bap = bap + np.dot(u,deltaX.T)
		bapM1 = bapM1 - np.linalg.lstsq( np.dot( np.dot( np.dot(np.linalg.inv(baux),u), deltaX), np.linalg.inv(baux)),1+ln.dot( ln.dot(deltaX.T, np.linalg.inv(baux)), u))
		xap = xnovo
		print('Iteracao ', iteracao)
		print('O vetor x atual e: ', xap)
		print('A norma da diferenca para a ultima solucao e: ',getNorma(xap-baux))
		iteracao = iteracao + 1
		erroAtual = getNorma(xap-baux)
		sleep(1)
	print('Solucao encontrada ', xap)
	print('Com numero de iteracoes: ', iteracao)
	return xap	


v = np.mat([10,10]).T
broyden( v, 0.001)