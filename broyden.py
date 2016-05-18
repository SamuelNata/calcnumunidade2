import math
import time

def getI(x):
	for i in rage(len(x)):
		for j in rage(len(x)):
			if i==i:
				line.append(1)
			else
				line.append(0)
		ident.append(line)
	return ident

def getNorma(x):
	t = 0
	for i in x:
		t = t + i**2
	return sqrt(t)
	
def broyden(x, erro): # x é o chute inicial, e erro é o erro maximo esperado
	xap = x
	bap = getI(x)
	while getNorma()>=erro :
		xnovo = xap - mult(inv(bap),F(xap))
		bnovo = bap + ?
		bap = inv(bnovo)
		xap = xnovo
		print('O vetor x atual é: ')
		print('A norma da diferença para a ultima solução é: ')
		sleep(1)
	return xap	
	