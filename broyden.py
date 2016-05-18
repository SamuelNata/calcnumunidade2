import math
import time

def getI(x):
	n = len(x)
	ident = numpy.zero(shape = (n,n))
	for i in rage(n):
		ident[i][i] = 1
	return ident

def getNorma(x):
	t = 0
	for i in x:
		t = t + i**2
	return sqrt(t)
	
	#todas as matrizes são iniciadas com string
def broyden(x, erro): # x é o chute inicial no formato de string, e erro é o erro maximo esperado
	xap = x
	bap = getI(x)
	while getNorma()>=erro :
		xnovo = xap - numpy.dot(inv(bap),F(xap))
		bnovo = bap + ?
		bap = inv(bnovo)
		xap = xnovo
		print('O vetor x atual é: ')
		print('A norma da diferença para a ultima solução é: ')
		sleep(1)
	return xap	
	