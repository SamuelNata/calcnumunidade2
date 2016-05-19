import math
import time
from utils import *
import numpy as np

def getI(x):
	n = x.shape[0]
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
	xap = np.asmatrix(x);
	print'xap'
	print xap
	print''
	bap = np.asmatrix(getI(x))
	print'bap'
	print bap
	print''
	bapM1 = np.asmatrix(getI(x))
	print'bapM1'
	print bapM1
	print''
	iteracao = 1
	erroAtual = 1000000

	while erroAtual>=erro :
		print 'np.dot(bapM1,F(xap))'
		print np.dot(bapM1,F(xap))
		print ''
		xnovo = xap - np.dot(bapM1,F(xap))
		print'xnovo'
		print xnovo
		print''
		deltaF = F(xnovo) - F(xap)
		print'deltaF'
		print deltaF
		print''
		deltaX = xnovo - xap
		print'deltaX'
		print deltaX
		print''

		print 'multiplicacao'
		print np.dot(deltaX,deltaX.T)
		print ''

		u = np.dot(np.linalg.inv(np.dot(deltaX,deltaX.T)), (deltaF-np.dot(bap,deltaX)))
		baux = bap*1 # para eles não passarem a aponter para o mesmo local da memoria
		print 'bap = ',bap
		print 'u = ',u
		print 'deltaX.T = ',deltaX.T
		bap = bap + np.dot(u,deltaX.T)
		bapM1 = bapM1 - np.linalg.lstsq( np.dot( np.dot( np.dot(np.linalg.inv(baux),u), deltaX), np.linalg.inv(baux)),1+ln.dot( ln.dot(deltaX.T, np.linalg.inv(baux)), u))
		xap = xnovo*1
		print('Iteracao ', iteracao)
		print('O vetor x atual e: ', xap)
		print('A norma da diferenca para a ultima solucao e: ',getNorma(xap-baux))
		iteracao = iteracao + 1
		erroAtual = getNorma(xap-baux)
		sleep(1)
	print('Solucao encontrada ', xap)
	print('Com numero de iteracoes: ', iteracao)
	return xap	


v = np.mat([1,3]).T
broyden( v, 0.001)